import arxiv
import arxiv # use !pip install arxiv
query = input("Subject/Author: ") # allows user to input whatever string they want

Choice = str(input("Choose which one you'd like to sort by: ")) 
sort_by = "None"

if Choice.lower() == "relevance":
    sort_by = arxiv.SortCriterion.Relevance
elif Choice.lower() == "submitted date":
    sort_by = arxiv.SortCriterion.SubmittedDate
elif Choice.lower() == "last updated":
    sort_by = arxiv.SortCriterion.LastUpdatedDate
else :
    Choice != "Relevance"
or "Submitted Date"
or "Last Updated"
print("Invalid input. Please try again.")

search = arxiv.Search(query = query, max_results = 10, sort_by = sort_by)

for result in search.results():
    print("Papers sorted by " + Choice + ": " + query + ": " + result.title)
