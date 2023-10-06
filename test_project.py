from project import Calendar

calendar = Calendar()

def test_add():
    assert calendar.add("2005-01-04", "It's my birthday!") == "\nAdded to the calendar 2005-01-04: It's my birthday!"
    assert calendar.add("2005-01-04", "Dinner out at McDonalds") == "\nAdded to the calendar 2005-01-04: Dinner out at McDonalds"
    assert calendar.add("2001-02-20", "It's my brother's birthday!") == "\nAdded to the calendar 2001-02-20: It's my brother's birthday!"
def test_edit():
    assert calendar.edit_event("2005-01-04", "It's my birthday!", 0, "Yep! That's my birthday") == "\nSuccessfully edited It's my birthday! on 2005-01-04"
    assert calendar.edit_event("2001-02-20", "It's my brother's birthday!", 0, "Yep! That's my brother's birthday") == "\nSuccessfully edited It's my brother's birthday! on 2001-02-20"
def test_delete():
    assert calendar.delete("2005-01-04", "Dinner out at McDonalds") == "\nSuccessfully deleted Dinner out at McDonalds within the date 2005-01-04."
    assert calendar.delete("2005-01-04", "Yep! That's my birthday") == "\nSuccessfully deleted all the task with the date 2005-01-04."


