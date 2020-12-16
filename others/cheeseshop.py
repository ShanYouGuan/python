def chesesshop(kind,*name, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in name:
        print(arg)
    print("-" * 30)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

chesesshop("Limburger", "It's very runny, sir.","It's really very, VERY runny, sir.",
shopkeeper="Michael Palin", client="John Cleese",sketch="Cheese Shop Sketch")