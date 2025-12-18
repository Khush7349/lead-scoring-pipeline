import pandas as pd
def score_role(title):
    title = title.lower()
    if "director" in title or "head" in title or "vp" in title:
        return 30
    elif "associate director" in title or "principal scientist" in title:
        return 20
    elif "senior scientist" in title:
        return 10
    else:
        return 0
def score_scientific_focus(focus):
    focus = focus.lower()
    if "drug-induced liver injury" in focus:
        return 40
    elif "3d" in focus or "organ-on-chip" in focus or "hepatic spheroids" in focus:
        return 30
    elif "investigative toxicology" in focus:
        return 20
    elif "general toxicology" in focus:
        return 10
    else:
        return 0
def score_publication(recent_pub):
    return 15 if recent_pub == "Yes" else 0
def score_funding(funding_status, company_type):
    if funding_status in ["Series B", "Public"] or company_type == "Big Pharma":
        return 20
    elif funding_status == "Series A":
        return 10
    elif funding_status == "Grant-funded":
        return 5
    else:
        return 0
def score_location(company_hq):
    hubs = ["cambridge","boston","san francisco","south san francisco","basel","london","oxford"]
    company_hq = company_hq.lower()
    return 10 if any(hub in company_hq for hub in hubs) else 0
def main():
    input_path = "../data/raw_leads.csv"
    output_path = "../output/ranked_leads.csv"
    df = pd.read_csv(input_path)
    df.columns = df.columns.str.strip().str.lower()
    df["role_score"] = df["title"].apply(score_role)
    df["scientific_score"] = df["scientific_focus"].apply(score_scientific_focus)
    df["publication_score"] = df["recent_publication"].apply(score_publication)
    df["funding_score"] = df.apply(lambda x: score_funding(x["funding_status"], x["company_type"]), axis=1)
    df["location_score"] = df["company_hq"].apply(score_location)
    df["probability_score"] = (df["role_score"]+ df["scientific_score"]+ df["publication_score"]+ df["funding_score"]+ df["location_score"])
    df["probability_score"] = df["probability_score"].clip(upper=100)
    df = df.sort_values(by="probability_score", ascending=False)
    df["rank"] = range(1, len(df) + 1)
    df.to_csv(output_path, index=False)
    print("Lead scoring complete. Ranked output saved.")
if __name__ == "__main__":
    main()
    