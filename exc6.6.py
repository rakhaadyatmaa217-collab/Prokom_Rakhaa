favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}
people_to_poll = ["jen", "sarah", "mike", "phil", "linda"]
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person.title()}.")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")
