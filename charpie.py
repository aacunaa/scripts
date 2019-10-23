# -*- coding: utf-8 -*- 
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["36% - Saas / Webmail",
          "22% - Pago",
          "18% - Finanzas",
          "9% - Otros",
          "3% - eCommerce / Retail",
          "3% - Cloud / Hosting",
          "3% - Logística / Shipping",
          "3% - Telecomunicaciones",
          "3% - Social Media"]

data = [float(x.split("%")[0]) for x in recipe]
wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-180)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, fontsize=16, **kw)

#ax.set_title("Mayores objetivos por industria 2q2019", fontsize=32)

plt.show()