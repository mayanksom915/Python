# # ---------- MATPLOTLIB FUNCTIONS AND PARAMETERS ----------


# MATPLOTLIB COLOR FUNCTIONS

# 1. color
#    Use: Line ka colour change karna.
 
#    plt.plot(x, y, color='red')

# 2. c
#    Use: Scatter points ka colour set karna.
 
#    plt.scatter(x, y, c='blue')

# 3. cmap
#    Use: Values ke according alag-alag colours dikhana.
 
#    plt.scatter(x, y, c=y, cmap='viridis')

# 4. edgecolor
#    Use: Bars ya markers ka border colour change karna.
 
#    plt.bar(x, y, edgecolor='black')

# 5. facecolor
#    Use: Figure ka background colour change karna.
 
#    plt.figure(facecolor='lightyellow')

# 6. markerfacecolor
#    Use: Marker ke andar ka colour change karna.
 
#    plt.plot(x, y, marker='o', markerfacecolor='yellow')

# 7. markeredgecolor
#    Use: Marker ke border ka colour change karna.
 
#    plt.plot(x, y, marker='o', markeredgecolor='black')


# ## 1. SIZE PARAMETERS

# 1. figsize
#    Use: Graph ki overall width aur height set karna.
#    plt.figure(figsize=(10, 5))

# 2. markersize
#    Use: Line graph ke markers ka size badhana ya ghatana.
#    plt.plot(x, y, marker='o', markersize=10)

# 3. fontsize
#    Use: Title aur labels ke text ka size set karna.
#    plt.title('My Graph', fontsize=16)

# 4. linewidth
#    Use: Line ki motai set karna.
#    plt.plot(x, y, linewidth=3)

# 5. s
#    Use: Scatter graph ke points ka size set karna.
#    plt.scatter(x, y, s=100)

# 6. width
#    Use: Bar graph ki bars ki width set karna.
#    plt.bar(x, y, width=0.5)

# ## 2. LINE STYLE PARAMETERS

# 7. linestyle
#    Use: Line ka style change karna.
#    plt.plot(x, y, linestyle='--')

# Common styles:
# '-'   = Solid line
# '--'  = Dashed line
# ':'   = Dotted line
# '-.'  = Dash-dot line

# 8. marker
#    Use: Line graph ke points par symbols lagana.
#    plt.plot(x, y, marker='o')

# Common markers:
# 'o' = Circle
# '*' = Star
# 's' = Square
# '^' = Triangle
# 'D' = Diamond
# '+' = Plus
# 'x' = Cross

# 9. alpha
#    Use: Graph element ki transparency set karna.
#    Value 0 se 1 ke beech hoti hai.
#    plt.plot(x, y, alpha=0.5)

# ## 3. GRAPH TYPES

# 10. plt.plot()
#     Use: Line graph banana.
#     plt.plot(x, y)

# 11. plt.bar()
#     Use: Vertical bar graph banana.
#     plt.bar(x, y)

# 12. plt.barh()
#     Use: Horizontal bar graph banana.
#     plt.barh(x, y)

# 13. plt.scatter()
#     Use: Data points ka graph banana.
#     plt.scatter(x, y)

# 14. plt.hist()
#     Use: Data distribution ka histogram banana.
#     plt.hist(data)

# 15. plt.pie()
#     Use: Pie chart banana.
#     plt.pie(values)

# 16. plt.boxplot()
#     Use: Data distribution aur outliers dekhna.
#     plt.boxplot(data)

# 17. plt.stackplot()
#     Use: Multiple data series ka stacked area graph banana.
#     plt.stackplot(x, y1, y2)

# 18. plt.step()
#     Use: Step-style graph banana.
#     plt.step(x, y)

# 19. plt.stem()
#     Use: Stem graph banana.
#     plt.stem(x, y)

# 20. plt.errorbar()
#     Use: Graph mein error bars dikhana.
#     plt.errorbar(x, y, yerr=errors)

# ## 4. TITLE, LABELS AND GRID

# 21. plt.title()
#     Use: Graph ka title set karna.
#     plt.title('Sales Report')

# 22. plt.xlabel()
#     Use: X-axis ka label set karna.
#     plt.xlabel('Months')

# 23. plt.ylabel()
#     Use: Y-axis ka label set karna.
#     plt.ylabel('Sales')

# 24. plt.legend()
#     Use: Graph ki legend dikhana.
#     plt.legend()

# 25. plt.grid()
#     Use: Graph mein grid lines dikhana.
#     plt.grid(True)

# 26. plt.xlim()
#     Use: X-axis ki minimum aur maximum limits set karna.
#     plt.xlim(0, 10)

# 27. plt.ylim()
#     Use: Y-axis ki minimum aur maximum limits set karna.
#     plt.ylim(0, 100)

# 28. plt.xticks()
#     Use: X-axis ke tick marks set karna.
#     plt.xticks([1, 2, 3, 4])

# 29. plt.yticks()
#     Use: Y-axis ke tick marks set karna.
#     plt.yticks([0, 20, 40, 60])

# 30. plt.text()
#     Use: Graph ke andar text likhna.
#     plt.text(2, 5, 'Hello')

# 31. plt.annotate()
#     Use: Kisi particular point ko label ya explain karna.
#     plt.annotate('Peak', xy=(2, 5))

# ## 5. PROFESSIONAL GRAPH FUNCTIONS

# 32. plt.style.use()
#     Use: Graph ki overall theme change karna.
#     plt.style.use('ggplot')

# 33. plt.colorbar()
#     Use: Graph ke saath colour scale dikhana.
#     plt.colorbar()

# 34. plt.bar_label()
#     Use: Bar ke upar uski value dikhana.
#     bars = plt.bar(x, y)
#     plt.bar_label(bars)

# 35. plt.axhline()
#     Use: Horizontal reference line draw karna.
#     plt.axhline(y=50)

# 36. plt.axvline()
#     Use: Vertical reference line draw karna.
#     plt.axvline(x=3)

# 37. plt.fill_between()
#     Use: Do lines ke beech ka area fill karna.
#     plt.fill_between(x, y1, y2)

# 38. plt.savefig()
#     Use: Graph ko image file mein save karna.
#     plt.savefig('graph.png')

# 39. plt.tight_layout()
#     Use: Graph ke elements ki spacing adjust karna.
#     plt.tight_layout()

# 40. plt.figure()
#     Use: Naya figure banana aur uska size set karna.
#     plt.figure(figsize=(8, 4))

# 41. plt.subplots()
#     Use: Figure aur axes create karna.
#     fig, ax = plt.subplots()

# 42. plt.subplot()
#     Use: Ek figure mein multiple graphs ki position set karna.
#     plt.subplot(1, 2, 1)

# 43. plt.suptitle()
#     Use: Multiple graphs ke liye common title set karna.
#     plt.suptitle('Sales Analysis')

# ## 6. AXIS AND TICKS FUNCTIONS

# 44. plt.tick_params()
#     Use: Axis ke tick marks ki appearance change karna.
#     plt.tick_params(axis='x', labelsize=12)

# 45. plt.xscale()
#     Use: X-axis ka scale change karna.
#     plt.xscale('log')

# 46. plt.yscale()
#     Use: Y-axis ka scale change karna.
#     plt.yscale('log')

# 47. plt.axhspan()
#     Use: Horizontal range ke beech shaded area banana.
#     plt.axhspan(20, 40, alpha=0.2)

# 48. plt.axvspan()
#     Use: Vertical range ke beech shaded area banana.
#     plt.axvspan(2, 4, alpha=0.2)

# ## 7. FIGURE AND AXES FUNCTIONS

# 49. plt.gca()
#     Use: Current axes ko access karna.
#     ax = plt.gca()

# 50. plt.gcf()
#     Use: Current figure ko access karna.
#     fig = plt.gcf()

# 51. plt.close()
#     Use: Figure ko close karna.
#     plt.close()

# 52. plt.clf()
#     Use: Current figure ko clear karna.
#     plt.clf()

# 53. plt.cla()
#     Use: Current axes ko clear karna.
#     plt.cla()

# 54. plt.show()
#     Use: Graph ko screen par display karna.
#     plt.show()

# ## 8. PIE CHART PARAMETERS

# 55. autopct
#     Use: Pie chart mein percentage show karna.
#     plt.pie(values, autopct='%1.1f%%')

# 56. explode
#     Use: Pie chart ke kisi slice ko alag dikhana.
#     plt.pie(values, explode=[0.1, 0, 0])

# 57. shadow
#     Use: Pie chart ke neeche shadow effect dena.
#     plt.pie(values, shadow=True)

# ## 9. IMPORTANT EXTRA PARAMETERS

# 58. edgecolor
#     Use: Bars ya markers ka border set karna.
#     plt.bar(x, y, edgecolor='black')

# 59. align
#     Use: Bar ki alignment set karna.
#     plt.bar(x, y, align='center')

# 60. bottom
#     Use: Bars ki starting vertical position set karna.
#     plt.bar(x, y, bottom=5)


