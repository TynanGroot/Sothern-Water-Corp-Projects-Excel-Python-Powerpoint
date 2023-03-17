#!/usr/bin/env python
# coding: utf-8

# <center><h1 style="color:#D4AF37"> ⚡⚡ AEMR Data Analysis ⚡⚡</h1>


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

get_ipython().run_cell_magic('capture', '', '!pip install ipython-sql sqlalchemy\nimport sqlalchemy\nsqlalchemy.create_engine("sqlite:///AEMR.db")\n%load_ext sql\n%sql sqlite:///AEMR.db')


# In[11]:


get_ipython().run_cell_magic('js', '', "require(['notebook/js/codecell'], function (codecell) {\n    codecell.CodeCell.options_default.highlight_modes['magic_text/x-mssql'] = { 'reg': [/%?%sql/] };\n    Jupyter.notebook.events.one('kernel_ready.Kernel', function () {\n        Jupyter.notebook.get_cells().map(function (cell) {\n            if (cell.cell_type == 'code') { cell.auto_highlight(); }\n        });\n    });\n});")



#  What are the most common outage types and how long do they tend to last? 
# How frequently do the outages occur? 
#  Are there any energy providers which have more outages than their peers which may be indicative of being unreliable? 

# Please note that throughout the entire case study, we are interested ONLY in the Outages where Status = Approved. We don't have any interest in Outages that were cancelled or not approved. This means your WHERE Clause will ALWAYS contain the field `Where Status = Approved` </u>


get_ipython().run_cell_magic('sql', '', "select count(outage_reason) as total_numer_of_outages, outage_reason, year\nfrom AEMR_outage_table\nwhere status = 'Approved'\nand year = '2016'\ngroup by outage_reason;\n\n\nselect count(outage_reason) as total_numer_of_outages, outage_reason, year\nfrom AEMR_outage_table\nwhere status = 'Approved'\nand year = '2017'\ngroup by outage_reason;")

# We note any behaviours across the months that indicate certain months having more reliability issues over other months

#  group the results by `Outage Type`, `Year` and `Month`. This is so you can identify whether there is any outage type specifically increasing on a monthly basis when comparing 2016 to 2017. </b>

get_ipython().run_cell_magic('sql', '', "select count(*) as outages, year, month\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by year, month\norder by year asc, month asc;")

# In other words, if an outage is very short, we aren't as concerned. However, if the outage is very long, this then has the risk of threatening our energy supplies. We want to identify the problematic energy providers here. This leads us to our next question below. 

# SQL statement that calculates 1) The `Total_Number_Outage_Events` and 2) The <b> `Average Duration`</b> in <u>DAYS</u> for each `Participant Code` and `Outage Type` over the 2016 and 2017 Period where the `Status = Approved`. 
# Order by `Total_Number_Outage_Events` in Descending Order, `Reason` and `Year`.

get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, count(*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, year\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, outage_reason\norder by total_number_of_outages desc, outage_reason, year")

# We classify a participant based off the following criteria:
#  High Risk - On average, the participant is unavailable for > 24 Hours (1 Day)</li>
#  Medium Risk - On average, the participant is unavailable between 12 and 24 Hours </li>
#  Low Risk - On average, the participant is unavailable for less than 12 Hours</li> 


#

get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, year, count (*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, \ncase\nwhen end_time-start_time > 24 then 'High Risk'\nwhen end_time-start_time between 24 and 15 then 'Med Risk'\nwhen end_time-start_time < 12 then 'low risk'\nend as 'risk'\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code\norder by avg_duration desc;")



get_ipython().run_cell_magic('sql', '', "select participant_code, outage_reason, year, count (*) as total_number_of_outages, \nround(AVG((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))), 2) as Avg_duration, \ncase\nwhen end_time-start_time > 24 or count(outage_reason = 'forced') > 20 then 'High Risk'\nwhen end_time-start_time between 24 and 15 or  count(outage_reason = 'forced') between 20 and 10 then 'Med Risk'\nwhen end_time-start_time < 12 or count(outage_reason = 'forced') < 10 then 'low risk'\nwhen outage_reason <> 'forced' then 'N/A'\nend as 'risk'\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, outage_reason\norder by total_number_of_outages desc, outage_reason, year;")


get_ipython().run_cell_magic('sql', '', "with force_outages as\n(select participant_code, year\nfrom AEMR_Outage_Table\nwhere status= 'approved'\nand outage_reason = 'Forced')\ngroup by participant_code,year\norder by year\nselect count(outage_reason) as total_outages, count(force_outages.participant_code) as Num_Forced_Outages, \nfrom AEMR_Outage_Table\nwhere status = 'approved'\ninner join force_outages on force_outages.year = AEMR_Outage_Table.year\ngroup by outage_reason")


# In[202]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM AEMR_Outage_Table')


# In[227]:


get_ipython().run_cell_magic('sql', '', "with F as(\nselect EventID, Outage_Reason as Num_Forced_Outages\nfrom AEMR_Outage_Table \nwhere Outage_Reason = 'Forced'\ngroup by EventID)\n\nselect AEMR_Outage_Table.year, count(Outage_reason) as Total_Outages,\n(count(F.Num_Forced_Outages)/count(AEMR_Outage_Table.outage_reason))*100 \nas Percent_Forced\nfrom AEMR_Outage_Table \nleft join f \non F.EventID = AEMR_Outage_Table.EventID\ngroup by year")





get_ipython().run_cell_magic('sql', '', "select participant_code, Facility_code, year, count(outage_reason) as _Total_Outages, \nsum((ABS(JULIANDAY(end_time) - JULIANDAY(start_time)))) as duration_in_days,\nsum(energy_lost_MW) as Total_Energy_Loss\nfrom AEMR_Outage_Table\nwhere status = 'Approved'\ngroup by participant_code, facility_code\norder by year desc")



# In[250]:


get_ipython().run_cell_magic('sql', '', "select year, Participant_code, Facility_code, round(AVG(ABS(JULIANDAY(end_time) - JULIANDAY(start_time))), 2) as Avg_duration, \nround(avg(Energy_Lost_MW),2) as Avg_Energy_Loss\nfrom Aemr_Outage_table\nwhere status = 'Approved'\nand outage_reason= 'Forced'\ngroup by year, Participant_code\norder by Avg_Energy_Loss desc;")


# <h3 style = "color:#5D3FD3"> Expected Output (Sample) </h3>
# 

# In[205]:

# <h4 style="color:Teal"> Please write your SQL in the code window below </h4>

# In[284]:


get_ipython().run_cell_magic('sql', '', "with f as (\nselect facility_code, sum(Energy_Lost_MW) as Energy_lost_by_force\n    from aemr_outage_table\n    where outage_reason = 'Forced'\n    group by facility_code)\n\nselect aemr_outage_table.facility_code, participant_code, year, round(Energy_lost_by_force / sum(Energy_lost_MW)*100, 2) as Perc_Energy_Lost, \nround(avg(energy_lost_MW),2) as Avg_Energy_lost, round(sum(energy_lost_MW),2) \nas total_energy_lost\nfrom AEMR_Outage_table\n join f on f.facility_code = aemr_outage_table.facility_code\ngroup by aemr_outage_table.facility_code\norder by total_energy_lost desc")




get_ipython().run_cell_magic('sql', '', "with a as\n    (select facility_code, participant_code, energy_lost_MW, description_of_outage, outage_reason,\n    (RANK() OVER (PARTITION BY participant_code\n    order by sum(energy_lost_MW) desc))\n    as rank_of_outage\n    from aemr_outage_table\n     group by participant_code, facility_code),\nbig_outage_r as (\n    select description_of_outage, outage_reason as biggest_reason, participant_code, facility_code, rank_of_outage, \n    energy_lost_MW as loss_of_r1\n    from a\n    where rank_of_outage = 1\n)\n\n\nselect rr.description_of_outage as Disc_of_biggest_out, rr.participant_code, rr.Facility_code, \nround(sum(aemr_outage_table.energy_lost_MW), 2) as total_energy_lost,  \nrank_of_outage, biggest_reason, round((loss_of_r1 / round(sum(aemr_outage_table.energy_lost_MW), 2)) * 100,2) \nas perc_of_total_loss\nfrom aemr_outage_table\ninner join big_outage_r as rr\non Aemr_outage_table.participant_code = rr.participant_code\nwhere Aemr_outage_table.participant_code = 'GW'\nor  Aemr_outage_table.participant_code = 'MELK'\nor  Aemr_outage_table.participant_code = 'AURICON'\ngroup by aemr_outage_table.participant_code, aemr_outage_table.facility_code;\n")

