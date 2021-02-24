

```python
import os
import csv
```


```python
budget_data_01=os.path.join("budget_data_1.csv")

```


```python
total_months = 0
total_revenue = 0
previous_revenue= 0
revenue_change_list = []
revenue_change_sum=[]



```


```python
with open(budget_data_01,newline='') as csvfile_01:
          
            csvreader_01= csv.DictReader(csvfile_01, delimiter=",") 
        #csvreader_01=csv.reader(csvfile_01)
            for row in csvreader_01:
                total_months = total_months + 1
                total_revenue = total_revenue + int(row['Revenue'])
                previous_revenue = int(row["Revenue"])
                revenue_change = int(row["Revenue"]) - previous_revenue
                revenue_change_list.append(row["Revenue"])
                revenue_change_sum=revenue_change + int(row['Revenue'])                       
                total_months_n=total_months-1

```


```python
#how should be 
#Financial Analysis
#----------------------------
#Total Months: 25
#Total Revenue: $1241412
#Average Revenue Change: $216825
#Greatest Increase in Revenue: Sep-16 ($815531)
#Greatest Decrease in Revenue: Aug-12 ($-652794)



print("Financial Analysis")
print("------------------------")
print("Total Revenue:"+" "+ str(total_revenue))
print("Total Months:"+ str(total_months))
print("Average Revenue Change:"+ str(revenue_change_sum/total_months_n))
print("Greatest Increase in Revenue: ("+ max(revenue_change_list)+")")
print("Greatest Decrease in Revenue:" +" "+ "("+ min(revenue_change_list)+")")


```

    Financial Analysis
    ------------------------
    Total Revenue: 18971412
    Total Months:41
    Average Revenue Change:22098.35
    Greatest Increase in Revenue: (977084)
    Greatest Decrease in Revenue: (-1172384)
    


```python

maxt=max(revenue_change_list)
index_max=revenue_change_list.index(maxt) 

index_max
```




    14




```python
mint=min(revenue_change_list)
index_min=revenue_change_list.index(mint) 
index_min
```




    22


