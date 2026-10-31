import pytest
from museum_admission import ticket_price, group_discount, gallery_entry

# ================= ticket_price =================
def test_adult_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300

def test_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("alien", 30, "tuesday", False)

def test_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)

def test_age_boundary_4_is_free():
    assert ticket_price("child", 4, "tuesday", False) == 0

def test_age_boundary_5_is_paid():
    assert ticket_price("child", 5, "tuesday", False) == 100

def test_age_zero_is_free():
    assert ticket_price("adult", 0, "tuesday", False) == 0

def test_monday_half_price():
    assert ticket_price("adult", 30, "monday", False) == 150

def test_saturday_surcharge():
    assert ticket_price("senior", 70, "saturday", False) == 250

def test_sunday_surcharge():
    assert ticket_price("adult", 30, "sunday", False) == 350

def test_weekday_not_monday_no_change():
    assert ticket_price("student", 20, "friday", False) == 150

def test_student_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200

def test_non_student_guided_tour():
    assert ticket_price("adult", 30, "tuesday", True) == 400

def test_monday_with_tour_combined():
    assert ticket_price("adult", 30, "monday", True) == 250

def test_weekend_student_with_tour():
    assert ticket_price("student", 20, "sunday", True) == 250

# ================= group_discount =================
def test_invalid_group_size_zero():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)

def test_invalid_group_size_negative():
    with pytest.raises(ValueError):
        group_discount(-3, True)

def test_group_size_1_valid():
    assert group_discount(1, False) == 0

def test_school_exactly_20():
    assert group_discount(20, True) == 40

def test_school_19():
    assert group_discount(19, True) == 25

def test_school_small():
    assert group_discount(5, True) == 25

def test_public_exactly_15():
    assert group_discount(15, False) == 20

def test_public_14():
    assert group_discount(14, False) == 10

def test_public_exactly_8():
    assert group_discount(8, False) == 10

def test_public_7():
    assert group_discount(7, False) == 0

# ================= gallery_entry =================
def test_gallery_at_capacity_waits():
    assert gallery_entry(100, 100, False) == "wait"

def test_gallery_over_capacity_waits():
    assert gallery_entry(120, 100, True) == "wait"

def test_gallery_90_percent_no_slot_queues():
    assert gallery_entry(90, 100, False) == "queue"

def test_gallery_90_percent_with_slot_enters():
    assert gallery_entry(90, 100, True) == "enter"

def test_gallery_just_below_90_percent_enters():
    assert gallery_entry(89, 100, False) == "enter"

def test_gallery_empty_enters():
    assert gallery_entry(0, 100, False) == "enter"
