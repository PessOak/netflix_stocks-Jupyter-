from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import matplotlib.ticker as mtick

# Let's load the datasets and inspect them.
netflix_stocks = pd.read_csv("NFLX.csv")
dowjones_stocks = pd.read_csv("DJI.csv")
netflix_stocks_quarterly = pd.read_csv("NFLX_daily_by_quarter.csv")
print(netflix_stocks_quarterly)

# let's look at the column names of the DataFrame netflix_stocks using .head()
netflix_stocks.head()

# Use Pandas to change the name of of the column to Adj Close to Price so that it is easier to work with the data. Remember to use inplace=True
# Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well
netflix_stocks.rename(columns={"Adj Close": "Price"}, inplace=True)
dowjones_stocks.rename(columns={"Adj Close": "Price"}, inplace=True)
netflix_stocks_quarterly.rename(columns={"Adj Close": "Price"}, inplace=True)

# Check the changes
netflix_stocks.head()

# In this step, we will be visualizing the Netflix quarterly data using violin plots! 
# add a title and change the labels 
# Pass the following arguments to sns.violinplot(): Quarter, Price and netflix_stocks_quarterly
ax = sns.violinplot(data=netflix_stocks_quarterly, x="Quarter", y="Price")
ax.set_title("NFLX stocks $ per quarter")
ax.set_xlabel("Business Quarters in 2017")
ax.set_ylabel("Closing Stock Price")

fmt = '${x:,.0f}' # Adding "$" units to the graphs
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
# plt.show()

x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual =[.4, .15,.29,.41]
earnings_estimate = [.37,.15,.32,.41 ]

# Next, we will chart the performance of the earnings per share (EPS) 
# By graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart.
# Add a legend, a tittle, change x_ticks, plot, set transparency alpha=0.5
plt.scatter(x_positions, earnings_actual, color="red", alpha=0.5)
plt.scatter(x_positions, earnings_estimate, color="blue", alpha=0.5)
plt.xticks(x_positions, chart_labels)
plt.legend(["Actual", "Estimate"])
plt.title("Earnings Per Share in Cents")
# plt.show()

# Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side
# Fill in the n, t, d, w values; plot the revenue bars; create a title and a legend; add labels

revenue_by_quarter = [2.79, 2.98,3.29,3.7] # The metrics below are in billions of dollars
earnings_by_quarter = [.0656,.12959,.18552,.29012]
quarter_labels = ["2Q2017","3Q2017","4Q2017", "1Q2018"]

# Revenue
n = 1
t = 2
d = 4
w = 0.8
bars1_x = [t*element + w*n for element
             in range(d)]
             
plt.bar(bars1_x, revenue_by_quarter)

# Earnings
n = 2
t = 2
d = 4
w = 0.8
bars2_x = [t*element + w*n for element
             in range(d)]

plt.bar(bars2_x, earnings_by_quarter)
middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
plt.xticks(middle_x, quarter_labels)
plt.title("Test 1")
plt.legend(["Revenue", "Earnings"])
plt.show()

# In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017 plotting line graphs side by side
# For each subplot, set_xlabel to "Date" and set_ylabel to "Stock Price". set titles for both of the plots
# There is some crowding in the Y axis labels, add some space by calling plt.subplots_adjust(wspace=.5)

# Left plot Netflix
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks["Date"], netflix_stocks["Price"])
ax1.set_title("Netflix")
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")


# Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks["Date"], dowjones_stocks["Price"])
ax2.set_title("Dow Jones")
ax2.set_xlabel("Date")
ax2.set_ylabel("Stock Price")

plt.rcParams.update({'font.size': 8})
plt.subplots_adjust(wspace=0.5)
plt.show()




