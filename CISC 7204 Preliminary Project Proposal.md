# Assessing Macau's Monthly Gross Gaming Revenue against Visitor Arrivals from 2019 to 2026

_CISC 7204 Preliminary Project Proposal_

| Field | Value |
|---|---|
|**Student ID**|MC 664973|
|**Name**|GU YUJIE|
|**Course Code**|CISC 7204|
|**Course Title**|Data Science and Data Visualization|
|**Coursework Item**|Assignment 01 - Preliminary Project Proposal|
|**Date**|20 September 2026|

This proposal asks a question about Macau's gaming economy that official government data can answer, and it sets out the datasets, tasks, and success criteria that will guide the work. Macau's gross gaming revenue fell by roughly four fifths in 2020, stayed depressed through 2022, and has recovered unevenly since the border reopened in January 2023. The proposal treats that recovery as a measurable relationship between two monthly series, visitor arrivals and gaming revenue, rather than as a narrative. The five sections below follow the CISC 7204 Project Proposal Guideline in order and satisfy the ideation requirements, so that the question stated here can be carried forward into Assignment 02.

## Project Topic Name

The project compares two monthly series that the Macau SAR Government publishes in full: gross gaming revenue and visitor arrivals. The title of the project is Assessing Macau's Monthly Gross Gaming Revenue against Visitor Arrivals from 2019 to 2026.

### Research Question

To what extent do monthly visitor arrivals explain month-to-month changes in Macau's monthly gross gaming revenue between January 2019 and the latest month published in 2026, and how much does the revenue generated per visitor differ between the pre-pandemic period (2019), the pandemic period (2020 to 2022), and the recovery period (2023 onwards)?

### Region and Domain Category

**Region:** Macau Special Administrative Region, China.

**Domain category:** tourism and the gaming industry, read through an economic and public-policy lens.

### Data Sources

Three published datasets cover the question, all of them on the Macau SAR Government Open Data Platform and all of them fully open. The first two are the ones the analysis depends on; the third is a supporting series that explains part of the capacity story.

**Monthly gross gaming revenue** (Gaming Inspection and Coordination Bureau, DICJ). Updated monthly; an Excel file recording the year, the month, monthly gross revenue in millions of patacas, and the year-on-year variance.

[https://data.gov.mo/Detail?id=f7c45dc2-80b4-468c-9e51-932bf60bd4cd](https://data.gov.mo/Detail?id=f7c45dc2-80b4-468c-9e51-932bf60bd4cd)

**Visitor arrivals** (Statistics and Census Service, DSEC). Updated monthly; published as a JSON series through the platform API, which allows the series to be pulled directly into the notebook rather than typed by hand.

[https://data.gov.mo/Detail?id=3546225a-2a34-4645-b01e-6752aed03993](https://data.gov.mo/Detail?id=3546225a-2a34-4645-b01e-6752aed03993)

**Number of casinos** (Gaming Inspection and Coordination Bureau, DICJ). An Excel file giving the count of licensed casinos, used to check whether changes in revenue track changes in capacity.

[https://data.gov.mo/Detail?id=a04f781e-48ec-4b5b-9014-599966652d3e](https://data.gov.mo/Detail?id=a04f781e-48ec-4b5b-9014-599966652d3e)

### How the Visualization Answers the Question

Two charts carry the answer. The first plots both series on a common index with the 2019 monthly average set to 100, so a reader sees at a glance how far each series fell, how much of its pre-pandemic level it has regained, and whether the two lines move together or drift apart. Indexing solves a presentational problem that would otherwise obscure the comparison, because the two variables are published in different units, millions of patacas and a count of people. The second chart is a scatter plot of monthly visitor arrivals against monthly gross gaming revenue, with the three periods coloured separately and a fitted line drawn for each. The slope of each line is the additional revenue associated with one more visitor in that period, so the chart answers the second half of the question directly: if the recovery-period points sit above the pre-pandemic line, visitors are generating more revenue per head than they used to, and if they sit below it, the return of visitors has not translated into a proportional return of revenue.

The remaining two figures support that reading rather than carry it. A month-by-year heatmap of revenue shows the seasonal pattern that would otherwise be mistaken for recovery or decline, and a short line chart of revenue per visitor tracks the ratio over time, so the reader can judge whether the gap between periods is stable or widening. Together the four figures are built so that the answer can be read from the visuals before the text is read; the written analysis then states what the figures show, where they are ambiguous, and what they cannot establish.

## Project Purpose

### Outcomes

The project works on the same learning outcomes that run through this course: collecting data from open sources, preparing it for analysis, exploring its structure, and communicating what it shows. It is also close to my major and to the local labour market. Macau's economy is unusually concentrated in gaming and tourism, so the ability to obtain, question, and visualize data from this sector is directly useful for analyst and research roles with integrated resort operators, the regulatory and statistical bodies that publish the figures, and consultancies working across the Greater Bay Area. The question is deliberately built to be extended rather than closed, because Assignment 02 continues from it: the same two series can support seasonal decomposition, a forecasting model, or a comparison across visitor source markets without changing the underlying data pipeline.

### Skills

- Locating, evaluating, and citing open government data, including both downloadable files and API endpoints.
- Cleaning and reshaping monthly time series in Python with pandas, including parsing year and month fields into dates, aligning two series on a common monthly index, and checking units.
- Exploratory data analysis of trends, seasonality, volatility, and outliers, and comparison across named periods.
- Designing charts that answer a specific question, including indexed line charts, heatmaps, and annotated scatter plots.
- Reasoning about correlation and simple regression, and keeping the distinction between association and causation intact when writing up results.
- Writing a short analytical argument that a reader with no background in the sector can follow.

### Knowledge

- What gross gaming revenue measures, how the DICJ aggregates it, and why monthly figures differ from the annual totals reported in the press.
- How DSEC defines and counts visitor arrivals, and what that definition leaves out.
- Descriptive statistics, index rebasing, and the seasonal structure typical of tourism data.
- Correlation and simple linear regression as tools for a two-variable question, together with their limits.
- The policy events that shape these particular series, including the pandemic border restrictions, the June 2022 outbreak, the 2022 concession re-tendering, and the January 2023 reopening.
- Data provenance in practice: units, revision risk, and the difference between a published statistic and an interpretation of it.

## Project Tasks

The work divides into six steps, each with a deliverable that the next step depends on.

1. **Acquire the data.** Download the DICJ monthly gross gaming revenue workbook, retrieve the DSEC visitor arrivals series through the platform API, and download the DICJ casino count workbook. Record the publisher, the download date, and the exact link for each. Deliverable: three raw data files and a source note.
2. **Prepare the data.** Parse the year and month fields into a single monthly date index, restrict the working table to January 2019 onwards, convert all revenue figures to one consistent unit, check for missing or repeated months, and merge the arrivals series onto the same index. Deliverable: a tidy monthly table and the script that produces it.
3. **Explore the data.** Describe the level, growth, and volatility of each series, compute year-on-year changes, examine the seasonal pattern, and annotate the events that visibly break the series. Deliverable: an exploratory section of the notebook with summary statistics and first plots.
4. **Produce the visualizations.** Build the four figures set out above: the indexed comparison of revenue and arrivals, the month-by-year heatmap, the period-coloured scatter with fitted lines, and the revenue-per-visitor chart. Deliverable: four figures saved as image files, each with a title, labelled axes, a stated index base, and a source note.
5. **Interpret and write up.** Answer the research question in about one page, quantify the recovery relative to 2019, report the arrivals-to-revenue relationship for each period, and state the limitations plainly. Deliverable: the written analysis.
6. **Assemble the final deliverable.** Package the work as one Jupyter notebook that runs from the raw downloads to the final figures, together with the written page. Deliverable: the notebook and the figures, arranged so that a reader can rerun the analysis.

### Guides, Worksheets and Requirements

This document is prepared against the CISC 7204 Project Proposal Guideline, and its five sections follow that guideline in order: the topic name and question, the purpose, the tasks, the criteria for success, and the collaboration position. The proposal ideation requirements are met in the section above, which states the region, the domain category, a question about that region and domain, the links to the available datasets, and a written justification of how the visualization answers the question. The submission requirements for Assignment 01 apply to the finished product: one MS-Word document of 2 to 5 A 4 pages, named CISC 7204-Assgn 01-MC 664973-PreliminaryProjectProposal.docx, submitted through the Individual Project Proposal submission link on the SUPPORT UMMoodle site for Class G, with the front page carrying the student ID, name, course code, course title, and coursework item. The analysis itself will be carried out in Python 3 with pandas and matplotlib in Jupyter Notebook, and every dataset will be cited in both the notebook and the written analysis.

## Project Criteria for Success

The finished work succeeds if a reader can answer the research question from the figures alone, and if every number in the analysis can be traced back to the published source.

- Reproducible. The notebook runs end to end from the published files and produces the same figures, with no step performed by hand and no figure edited after export.
- Relevant. Each figure addresses part of the stated question; nothing is included for decoration.
- Legible. Titles, axis labels, units and the index base are stated, periods are distinguished consistently, and the charts remain readable at the size they are printed.
- Statistically honest. Revenue and arrivals are never combined without unit checks, correlation is reported per period rather than pooled, and no causal claim is made from an association.
- Complete against the brief. The finished deliverable meets the required page range and file name, shows the required front-page information, and cites its sources.

As the guideline asks, the criteria above will be evidenced by the final visual rather than by a separate rubric or checklist: a four-panel figure combining the four charts into one view is the main device for telling the story of the data.

## Project Collaboration

This is an individual project, so the collaboration issues the guideline raises, which are written for team-based projects, do not apply: there is no division of work among members, no group structure to define, and no team ground rules to agree. The work is carried out and reviewed by me alone, with the scope fixed before any code is written and the result reviewed against the criteria above at the end of each step.