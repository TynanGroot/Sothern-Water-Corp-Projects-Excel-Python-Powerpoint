#!/usr/bin/env python
# coding: utf-8

# <center><h1 style="color:#D4AF37"> ⚡⚡ AEMR Data Analysis ⚡⚡</h1>

# <img src = "https://images.squarespace-cdn.com/content/v1/551972d8e4b0d571edc2e2c8/8f3abd33-0916-4415-9b24-593eea1d1e3c/Screen+Shot+2022-04-20+at+12.41.24+PM.png">
# 
#   
# It’s time for you to apply your budding SQL Competencies to analyse data for the American Energy Market Regulator (AEMR).
# 
# You'll be writing <b> SQL </b> in this Jupyter Notebook and then preparing to save the results from your SQL queries as `.csv` files you'll be using in the next step for your `Tableau` Analysis!
# 
# The analytics team has supplied you with the following table extract that contains all the data you need to analyse for the `AEMR` outages. 
# 
# <li> AEMR_Outage_Table </li> 
#     
# Now let's revisit the business problem below and understand what we're seeking to solve.

# <h1 style="color:#D4AF37"> What's the Business Problem? 💰</h1>
# 
# The American Energy Market Regulator (AEMR) is responsible for looking after the
# United States of America’s domestic energy network. The regulator’s responsibility is to
# ensure that America’s energy network remains reliable with minimal disruptions, which
# are known as outages. 
# 
# There are four key types of outages:
# 
# ● Consequential
# 
# ● Forced 
# 
# ● Opportunistic 
# 
# ● Planned 
# 
# Recently, the AEMR management team has been increasingly aware of a large number
# of energy providers that submitted outages over the 2016 and 2017 calendar years. The
# management team has expressed a desire to have the following two areas of concern
# addressed:
# 
# <b> A) Energy Stability and Market Outages
#     <p>
# B) Energy Losses and Market Reliability </b>
# 
# As an analyst within the data and reporting team, you have been asked to address these
# two immediate areas of concern. Feel free to also explore beyond the queries asked and provide additional insights that you feel may be of interest to the management team. 

# <h3 style="color:#D4AF37">  SQLite Refresher ⚙️ </h3>
# 
# We've pre-loaded the data you need to access in the `AEMR.db` we've included. We'll have you write SQL below where all your SQL queries will be stored in this notebook as a reference you can use when you review your data analysis in Tableau. </b>.
# 
# To load the `AEMR.db` file into this notebook, run the below cells.
# 
# <b> ⚠️ Please remember that everytime you close this file and re-open this, you'll need to re-run the cells below. ⚠️ </b>

# <b>⚠️ Note: Remember, you'll need to start each cell with the **`%%sql`** line, which allows us to execute SQL from within this notebook.</b>

# In[10]:


get_ipython().run_cell_magic('capture', '', '!pip install ipython-sql sqlalchemy\nimport sqlalchemy\nsqlalchemy.create_engine("sqlite:///AEMR.db")\n%load_ext sql\n%sql sqlite:///AEMR.db')


# In[11]:


get_ipython().run_cell_magic('js', '', "require(['notebook/js/codecell'], function (codecell) {\n    codecell.CodeCell.options_default.highlight_modes['magic_text/x-mssql'] = { 'reg': [/%?%sql/] };\n    Jupyter.notebook.events.one('kernel_ready.Kernel', function () {\n        Jupyter.notebook.get_cells().map(function (cell) {\n            if (cell.cell_type == 'code') { cell.auto_highlight(); }\n        });\n    });\n});")


# We've included an example of how you would write a query against the database below:
# 
# ~~~sql
# %%sql
# SELECT
# *
# FROM AEMR_Outage_Table
# LIMIT 10
# ~~~
# 
# Once you've written your SQL, you'll then need to press `Ctrl` + `Enter` to run the cell.
# Otherwise, you can just press `run` at the very top of your screen, to run the specific cell.
# 
# For your convenience, we've included a <b style = "color:#5D3FD3"> subset of the answers </b> under the header `Expected Output (Sample)`. These small subsets also include all the `columns` you'll need to include in your Query, so you know what to expect!
# 
# Good luck!

# <h3 style="color:#D4AF37"> ⚡ Part I. Energy Stability & Market Outages ⚡ </h3>
# 
# Energy stability is one of the key themes the AEMR management team cares about. To ensure energy security and reliability, AEMR needs to understand the following:
# <p>
# <b>
# 
# <li> What are the most common outage types and how long do they tend to last? 
# <li> How frequently do the outages occur? 
# <li> Are there any energy providers which have more outages than their peers which may be indicative of being unreliable? 
#     
# <p>
# 
# <u style="color:Maroon"> Please note that throughout the entire case study, we are interested ONLY in the Outages where Status = Approved. We don't have any interest in Outages that were cancelled or not approved. This means your WHERE Clause will ALWAYS contain the field `Where Status = Approved` </u>

# <h3 style="color:#D4AF37"> Question One </h3> 
# 
# <b> Write a SQL Statement to `COUNT` the number of valid (i.e. `Status = Approved`) Outage Events sorted by their respective `Outage_Reason` (i.e. `Forced`, `Consequential`, `Scheduled`, `Opportunistic`) over the 2016 & 2017 Periods. </b>
# 
# Do we notice anything regarding the trends for specific Outages over the 2016 / 2017 Period?

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# <b>⚠️ Note: Remember, you'll need to start each cell with the **`%%sql`** line, which allows us to execute SQL from within this notebook.</b>

# In[27]:


get_ipython().run_cell_magic('sql', '', "select count(outage_reason) as total_numer_of_outages, outage_reason, year\nfrom AEMR_outage_table\nwhere status = 'Approved'\nand year = '2016'\ngroup by outage_reason;\n\n\nselect count(outage_reason) as total_numer_of_outages, outage_reason, year\nfrom AEMR_outage_table\nwhere status = 'Approved'\nand year = '2017'\ngroup by outage_reason;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[194]:





# Now how about examining some monthly trends? Do we note any behaviours across the months that indicate certain months having more reliability issues over other months? 
# 

# <h3 style="color:#D4AF37"> Question Two </h3>
# 
# 

# <b> i) Write a SQL Statement showing the `Total` of all Outage Types (Forced, Consequential, Scheduled, Opportunistic) where the `Status = Approved`, that occurred for both 2016 and 2017, grouped by `Year` and `Month`.  per month (i.e. 1 – 12). Order by `Year`, `Month`, `Total_Number_Outages` in Descending Order.
# 
# 
# ii) Building on the query you write in i), group the results by `Outage Type`, `Year` and `Month`. This is so you can identify whether there is any outage type specifically increasing on a monthly basis when comparing 2016 to 2017. </b>
# 
# 
# <b>⚠️Hint: You might find it helpful to create a small Common Table Expression to address these two questions! </b>

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[34]:


get_ipython().run_cell_magic('sql', '', "select count(*) as outages, year, month\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by year, month\norder by year asc, month asc;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[3]:





# Hmm. Interesting. We've now identified a specific outage type is rapidly increasing from 2016 to 2017. However, frequency is just one aspect we care about. We also care about the <b> `duration` </b> of our ouatges.
# 
# In other words, if an outage is very short, we aren't as concerned. However, if the outage is very long, this then has the risk of threatening our energy supplies. We want to identify the problematic energy providers here. This leads us to our next question below. 

# <h3 style="color:#D4AF37"> Question Three </h3>
# 

# <b>Write a SQL statement that calculates 1) The `Total_Number_Outage_Events` and 2) The <b> `Average Duration`</b> in <u>DAYS</u> for each `Participant Code` and `Outage Type` over the 2016 and 2017 Period where the `Status = Approved`. 
# Order by `Total_Number_Outage_Events` in Descending Order, `Reason` and `Year`.
#     
# Please note the average duration in days should be rounded to 2 decimal places for ease of comparison. When calculating the average duration, please note that you'll need to use the following fields:
# 
# `Start_Time` and `End_Time`. </b>
# 
# <b>⚠️ Hint:</b> If you're not sure how to calculate the difference between the `start_time` and `end_time` , reference this link <a href ="https://learnsql.com/cookbook/how-to-calculate-the-difference-between-two-timestamps-in-sqlite/"> here </a>
# 
# We've included an example below of how you could use the `JULIANDAY()` function! Remember, the `JULIANDAY()` function returns the results in days, including the fractional component. Some of the date(s) are flipped in the dataset, so you'll need to use the ABS() function to ensure you don't return any negative values!
# 
# ~~~sql
# %%sql
# 
# SELECT
#         AVG((ABS(JULIANDAY(Date_2) - JULIANDAY(Date1))) 
# FROM Some_Database
# ~~~
# 
# 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[56]:


get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, count(*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, year\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, outage_reason\norder by total_number_of_outages desc, outage_reason, year")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[196]:





# Now we're getting somewhere...!
# We've identified participants who are having many outages, as well as participants who have been offline for the longest durations.
# 
# Armed with this information, it's important we're able to classify our participants accordingly based on reliability metrics of uptime.
# 
# We classify a participant based off the following criteria:
# <b>
# <li> High Risk - On average, the participant is unavailable for > 24 Hours (1 Day)</li>
# <li> Medium Risk - On average, the participant is unavailable between 12 and 24 Hours </li>
# <li> Low Risk - On average, the participant is unavailable for less than 12 Hours</li> 
# </b>

# <h3 style="color:#D4AF37"> Question Four </h3>

# <b> Using the above criteria for context, write a SQL Statement that <u> classifies each participant code as either `High Risk`, `Medium Risk` or `Low Risk` in a column called `Risk_Classification`</u> that is based off their Average Outage Duration Time. Please note that this is for all valid (i.e. `Where status = approved`) outage types (Forced, Consequential, Scheduled, Opportunistic) for <u>all</u> participant codes from 2016 to 2017. Order the results using `Average Duration Time In Days` in descending order. 
# 
# <b>⚠️Hint: Think about the CASE Statement and how you might use this to help you with your classification! This is a more challenging question so you'll need to think through this step by step. You might also find `CTEs` or `Sub Queries` helpful for you.</b>
# 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[82]:


get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, year, count (*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, \ncase\nwhen end_time-start_time > 24 then 'High Risk'\nwhen end_time-start_time between 24 and 15 then 'Med Risk'\nwhen end_time-start_time < 12 then 'low risk'\nend as 'risk'\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code\norder by avg_duration desc;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[201]:





# Now that we've classified our participants as either `High Risk`, `Medium Risk` or `Low Risk`, we want to dig a little deeper.
# 
# Does it make sense that `Consequential`, `Opportunistic` or `Planned` aren't considered regarding the Risk Category?
# 
# Perhaps we should refine our category accordingly by ensuring we focus our Risk Category on labelling only `Forced` Outages as being a Risk. After all, Forced Outages are the unplanned outages that risk the security of the electricity grid.
# 
# Let's add two additional criteria to our classification considering `Total Number of Outage Events` and `Outage Type`.
# 
# We've summarised these below:
# 
# <b>
# <li> High Risk - On average, the participant is unavailable for > 24 Hours (1 Day) OR the Total Number of Outage Events > 20 </li>
# <li> Medium Risk - On average, the participant is unavailable between 12 and 24 Hours OR the Total Number of Outage Events is Between 10 and 20 </li>
# <li> Low Risk - On average, the participant is unavailable for less than 12 Hours OR the Total Number of Outage Events < 10 </li> 
# <li> If Outage Type is not forced, then N/A
# </b>
# 

# <h3 style="color:#D4AF37"> Question Five </h3>

# <b> Just as you did in Question Four, Using the above criteria for context, write a SQL Statement that <u> classifies each participant code as either `High Risk`, `Medium Risk` or `Low Risk` in a column called `Risk_Classification`</u> using the new classification criteria. Order the results using `Average Duration Time In Days` in descending order. 
# 
# <b>⚠️Hint: Think about the CASE Statement and how you might use this to help you with your classification! </b>
# 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[145]:


get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, year, count (*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, \ncase\nwhen end_time-start_time > 24 or count(outage_reason = 'forced') > 20 then 'High Risk'\nwhen end_time-start_time between 24 and 15 or  count(outage_reason = 'forced') between 20 and 10 then 'Med Risk'\nwhen end_time-start_time < 12 or count(outage_reason = 'forced') < 10 then 'low risk'\nwhen outage_reason <> 'forced' then 'N/A'\nend as 'risk'\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, outage_reason\norder by total_number_of_outages desc, outage_reason, year;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>

# In[202]:





# <h3 style="color:#D4AF37"> ⚡ Part II. Energy Losses & Market Reliability ⚡ </h3>

# When an energy provider provides energy to the market, they are making a commitment to the market and saying; “We will supply X amount of energy to the market under a contractual obligation.” However, in a situation where the outages are Forced, the energy provider intended to provide energy but are unable to provide energy and are forced offline. <b style="color:Maroon">If many energy providers are forced offline at the same time it could cause an energy security risk that AEMR needs to mitigate. </b>
# 
# To ensure this doesn’t happen, the AEMR is interested in exploring the following questions:
# 
# <li> Of the outage types in 2016 and 2017, what percent were Forced Outage(s)?
# <li> What was the average duration for a forced outage during both 2016 and 2017? Have we seen an increase in the average duration of forced outages?
# <li> Which energy providers tended to have the largest number of forced outages?
#     
# <p>
# 
# <b> We'll examine this in the questions below. </b>
#     
# <img src = "https://media.istockphoto.com/id/1281821795/photo/market-stock-graph-and-information-with-city-light-and-electricity-and-energy-facility-banner.jpg?s=612x612&w=0&k=20&c=RSN5LqeMW28HW10aA190_DWR5YJ5tG2wixHFPBV3uZE=">

# <h3 style="color:#D4AF37"> Question Six </h3>

# <b> Write a SQL Statement to calculate the proportion of Forced Outages that have occurred over the 2016 - 2017 Period.
# Do we observe any particular increases regarding any Outage Types over this period? </b>

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[177]:


get_ipython().run_cell_magic('sql', '', "with force_outages as\n(select participant_code, year\nfrom AEMR_Outage_Table\nwhere status= 'approved'\nand outage_reason = 'Forced')\ngroup by participant_code,year\norder by year\nselect count(outage_reason) as total_outages, count(force_outages.participant_code) as Num_Forced_Outages, \nfrom AEMR_Outage_Table\nwhere status = 'approved'\ninner join force_outages on force_outages.year = AEMR_Outage_Table.year\ngroup by outage_reason")


# In[202]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM AEMR_Outage_Table')


# In[227]:


get_ipython().run_cell_magic('sql', '', "with F as(\nselect EventID, Outage_Reason as Num_Forced_Outages\nfrom AEMR_Outage_Table \nwhere Outage_Reason = 'Forced'\ngroup by EventID)\n\nselect AEMR_Outage_Table.year, count(Outage_reason) as Total_Outages,\n(count(F.Num_Forced_Outages)/count(AEMR_Outage_Table.outage_reason))*100 \nas Percent_Forced\nfrom AEMR_Outage_Table \nleft join f \non F.EventID = AEMR_Outage_Table.EventID\ngroup by year")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[203]:





# Great. It's clear to see now that `Forced Outages` are problematic for us. Not only are they the only outage type that generates financial losses as the Outage is unplanned, it seems there is a number of Energy Participants who have been having a significantly high number of Outages.
# 
# Now what can we do about this? 
# 
# Let's break our analysis down into Macro and Micro Analysis.
# The total gives us the Overall Duration a participant is offline / has lost energy, however, it doesn't tell us how *frequently* this occurs. In other words, if we have one or two very big outages, it might contribute to very large totals.
# 
# However, perhaps an <b> average </b> can help us identify how big these Outages might really be, spread across the year!
# 
# Let's take a look.

# <h3 style="color:#D4AF37"> Question Seven </h3>

# Write a SQL Statement to calculate the `Total Number of Outages`, `Total Duration In Days`and `Total Energy Lost` of all valid `Outages` for each `participant code` and `facility_code`, sorted by `Total Energy Lost` in descending order and Ordered by the YEAR Category. 
#     

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[236]:


get_ipython().run_cell_magic('sql', '', "select participant_code, Facility_code, year, count(outage_reason) as _Total_Outages, \nsum((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))) as duration_in_days,\nsum(energy_lost_MW) as Total_Energy_Loss\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, facility_code\norder by year desc")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[204]:





# <h3 style="color:#D4AF37"> Question Eight </h3>

# <b> Write a SQL Statement to calculate the `Average Duration In Days`and `Average Energy Lost` of all valid `FORCED OUTAGES` for each `participant code` and `facility_code` sorted by `Average Energy Lost` in descending order and Ordered by the YEAR Category. 
# 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[250]:


get_ipython().run_cell_magic('sql', '', "select year, Participant_code, Facility_code, round(AVG(ABS(JULIANDAY(end_time) - JULIANDAY(start_time))), 2) as Avg_duration, \nround(avg(Energy_Lost_MW),2) as Avg_Energy_Loss\nfrom Aemr_Outage_table\nwhere status = 'Approved'\nand outage_reason= 'Forced'\ngroup by year, Participant_code\norder by Avg_Energy_Loss desc;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[205]:





# <h3 style="color:#D4AF37"> Question Nine </h3>

# <b> Write a SQL Statement to calculate the `Average Energy Lost` and `Total Energy Lost` for each `Facility Code` and `Participant Code` across both the 2016 and 2017 periods when the `Outage_Reason` is set to Forced. Upon completion of this, calculate the <u> percentage </u> of energy lost due to forced outages for each `Facility_Code`. Please ORDER the query by `Total Energy Lost` from 2016 to 2017.
#     
# From your analysis, which participants have contributed the most to the Energy Lost due to Forced Outages?
# 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[284]:


get_ipython().run_cell_magic('sql', '', "with f as (\nselect facility_code, sum(Energy_Lost_MW) as Energy_lost_by_force\n    from aemr_outage_table\n    where outage_reason = 'Forced'\n    group by facility_code)\n\nselect aemr_outage_table.facility_code, participant_code, year, round(Energy_lost_by_force / sum(Energy_lost_MW)*100, 2) as Perc_Energy_Lost, \nround(avg(energy_lost_MW),2) as Avg_Energy_lost, round(sum(energy_lost_MW),2) \nas total_energy_lost\nfrom AEMR_Outage_table\n join f on f.facility_code = aemr_outage_table.facility_code\ngroup by aemr_outage_table.facility_code\norder by total_energy_lost desc")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[206]:





# <h3 style="color:#D4AF37"> Question Ten </h3>

# <b>Having identified the top 3 participants by Total Energy Loss being `GW`, `MELK` and `Auricon`; Write a SQL Statement calculating the `Total_Energy_Lost` each of these three `Participant_Codes` and the `Facility_Code`. Additionally, identify the `Description_Of_Outage` associated with the highest `Total_Energy_Lost` for each of the `Participant_Codes` and `Facility_Code` for each of the three participants. 
#     
# <u>Lastly, calculate the percentage of Energy Loss, attributed to these reasons!</u> </b>
# 
# <b> ⚠️ Hint: As this is the final question, this is a bit of a <b> challenge question </b> which will involve some SQL functions you're not familiar with just yet. In the workplace, you're going to have to grow familiar with googling and searching for functions that you may have not learned or be familiar with. In this question, to identify the TOP `Description_Of_Outage` reason for each Participant, you're going to need to use `PARTITION BY`. You can read all about the approach you can take in this example <a href = "https://learnsql.com/cookbook/how-to-rank-rows-within-a-partition-in-sql/#:~:text=To%20partition%20rows%20and%20rank,rank%20rows%20within%20a%20partition."> here </a>. Good luck! 

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[395]:


get_ipython().run_cell_magic('sql', '', "with a as\n    (select facility_code, participant_code, energy_lost_MW, description_of_outage, outage_reason,\n    (RANK() OVER (PARTITION BY participant_code\n    order by sum(energy_lost_MW) desc))\n    as rank_of_outage\n    from aemr_outage_table\n     group by participant_code, facility_code),\nbig_outage_r as (\n    select description_of_outage, outage_reason as biggest_reason, participant_code, facility_code, rank_of_outage, \n    energy_lost_MW as loss_of_r1\n    from a\n    where rank_of_outage = 1\n)\n\n\nselect rr.description_of_outage as Disc_of_biggest_out, rr.participant_code, rr.Facility_code, \nround(sum(aemr_outage_table.energy_lost_MW), 2) as total_energy_lost,  \nrank_of_outage, biggest_reason, round((loss_of_r1 / round(sum(aemr_outage_table.energy_lost_MW), 2)) * 100,2) \nas perc_of_total_loss\nfrom aemr_outage_table\ninner join big_outage_r as rr\non Aemr_outage_table.participant_code = rr.participant_code\nwhere Aemr_outage_table.participant_code = 'GW'\nor  Aemr_outage_table.participant_code = 'MELK'\nor  Aemr_outage_table.participant_code = 'AURICON'\ngroup by aemr_outage_table.participant_code, aemr_outage_table.facility_code;\n")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[198]:





# Well done! That's a Wrap! We've now analyzed all the data we need to answer Management's Question.
# You'll now move to the next part of your analysis where you'll be proceeding with creating your story in Tableau using the insights you've gathered from your SQL Analysis! 
# 
# Let's now switch to Part II of our Analysis in Tableau!!
# 
# <img src = https://www.energymagazine.com.au/wp-content/uploads/2021/05/shutterstock_1888482466-e1620278098312.jpg>
# 

# ## Appendix: SQL Cheat Sheet
# 
# **SELECT**
# 
# ```SQL
# - SELECT * FROM table_name -- Select all columns from a table
# - SELECT column_name(s) FROM table_name -- Select some columns from a table
# - SELECT DISTINCT column_name(s) FROM table_name -- Select only the different values
# - SELECT column_name(s) FROM table_name -- Select data filtered with the WHERE clause
#   WHERE condition
# - SELECT column_name(s) FROM table_name -- Order data by multiple columns. DESC for descending 
#   ORDER BY column_1, column_2 DESC, column_3 ASC -- and ASC (optional) for ascending order
# ```
# 
# **Operators**
# - `<` - Less than
# - `>` - Greater than
# - `<=` - Less than or equal
# - `>=` - Greater than or equal
# - `<>` - Not equal
# - `=` - Equal
# - `BETWEEN v1 AND v2` - Between a specified range
# - `LIKE` - Search pattern. Use `%` as a wildcard. E.g., `%o%` matches "o", "bob", "blob", etc.
# 
# **Aggregate Functions**
# - `AVG(column)` - Returns the average value of a column
# - `COUNT(column)` - Returns the number of rows (without a NULL value) of a column
# - `MAX(column)` - Returns the maximum value of a column
# - `MIN(column)` - Returns the minimum value of a column
# - `SUM(column)` - Returns the sum of a column
# ```SQL
# SELECT AVG(column_name), MIN(column_name), MAX(column_name) FROM table_name
# ```
#  
# **Miscellaneous**
# - `CASE...END` - Used in `SELECT` queries to alter a variable in place. E.g.
# ```SQL
# SELECT column_name
#     CASE
#         WHEN column_name >= 0 THEN 'POSITIVE'
#         ELSE 'NEGATIVE'
#     END
# FROM table
# ```
# - `AS` - Used to rename a variable. E.g.
# ```SQL
# SELECT SUM(column_name) AS total_column_name FROM table_name
# ```
# - `GROUP BY` - Used to group rows that share the same value(s) in particular column(s). It is mostly used along with aggregation functions
# - `ORDER BY` - Determines the order in which the rows are returned by an SQL query
