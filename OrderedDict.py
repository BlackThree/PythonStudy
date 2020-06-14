from collections import OrderedDict

favoriteLangs = OrderedDict()
favoriteLangs["jen"] = "python"
favoriteLangs["sarah"] = "c"

for name, language in favoriteLangs.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

