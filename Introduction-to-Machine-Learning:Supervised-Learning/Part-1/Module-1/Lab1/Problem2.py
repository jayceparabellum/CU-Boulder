
df = load_housing()

#####Personal code starts here####
q25 = df ["MedInc"].quantile(.25)
q75 = df ["MedInc"].quantile(0.75)

bottom = df[df["MedInc"] <= q25]
top = df[df["MedInc"] >= q75]

bottom_mean = bottom["MedhouseVal"].mean()
top_mean = top["MedHouseVal"].mean()

q2_income_value_gap: float = round(top_mean - bottom_mean, 3)

print(f"Income value gap: {q2_income_value_gap}")
#####Personal code ends above#####

raise NotImplementedError
