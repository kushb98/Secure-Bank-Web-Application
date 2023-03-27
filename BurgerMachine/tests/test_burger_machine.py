import pytest
import random
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

# sample fixture, can delete if not using
@pytest.fixture
def first_order(machine):
    machine.handle_bun("no bun")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

# sample fixture, can delete if not using
@pytest.fixture
def second_order(first_order):
    first_order.handle_bun("lettuce wrap")
    first_order.handle_patty("turkey")
    first_order.handle_patty("turkey")
    first_order.handle_patty("next")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("cheese")
    first_order.handle_toppings("done")
    #machine.handle_pay(10000,"10000")
    return first_order

# sample test case, can delete if not using
def test_production_line(second_order):
    for j in second_order.buns:
        print(second_order.inprogress_burger)
        if j.name.lower() == second_order.inprogress_burger[0].name.lower():
            assert True
            return

    assert False

# add required test cases below
def test1_first_bun(machine):
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_patty('veggie')
        machine.pick_toppings('tomato')
    except InvalidStageException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
# hip2 and 03/20/23 Description: This method first counts the length of the inprogress burger then adds patty and toppings in the try block, but as patty and toppings can not 
# be added until a selection of bun is made that's why its going in exception state ie.InvalidStageException and in finally the len of inprogress burger(previous one we counted in 
# beginning) is matched with current's inprogress burger length in assert so the test case will work if only those two matched. 

def test_2_patty_in_stock(machine):
    machine.patties[0].quantity = 0
    name = machine.patties[0].name.lower()
    machine.handle_bun('no bun')
    before_inprog_lst_length = len(machine.inprogress_burger)
    #machine.currently_selecting = BurgerMachine.STAGE.patties
    try:
        machine.pick_patty(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))   
# hip2 and 03/20/23 Description: This test case determines whether or not a patty is in stock, so to test it, I set the amount of the first patty, Turkey, to zero and sent it to 
# the name variable and the amount is set to zero before selecting a bun using the machine, and in the try block, I choose this patty which wont execute and go to catch block
# and function should issue an OutOfStockException and if it does, the test case is successful. Also the same finally state is executed in every test case.

def test_3_topping_in_stock(machine):
    machine.toppings[2].quantity = 0
    name = machine.toppings[2].name.lower()
    machine.handle_bun('white burger bun')
    machine.handle_patty('beef')
    machine.handle_patty('veggie')
    machine.handle_patty('next')
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_toppings(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
## hip2 and 03/20/23 Description: This test case determines whether or not a topping is in stock or not so to test it, I set the amount of the third topping tomato to zero & set it to 
# the name variable and the amount is set to zero before selecting a bun using the machine. then i added bun and patties and finally in the try block, I choose this tomato which 
# wont execute and go to catch blockand function should issue an OutOfStockException and if it does, the test case is successful. Also the same finally state is executed in every
# test case.
        
def test_4_add_3_patties(machine):
    machine.handle_bun('no bun')
    machine.pick_patty('veggie')
    machine.pick_patty('beef')
    machine.pick_patty('beef')
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_patty('veggie')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
## hip2 and 03/20/23 Description:The above test case makes a burger by selecting a bun and three patties, with a maximum limit of three patties per order as number of max patties are initialized to 3 in burgermachine.py
# After that, I'm calculating the length of the in-progress burger, and in the try except block, I'm adding the fourth patty. If we get the ExceededRemainingChoicesException, 
# the test case is successful.


def test_5_add_3_toppings(machine):
    machine.handle_bun('no bun')
    machine.handle_patty('beef')
    machine.handle_patty('veggie')
    machine.handle_patty('next')
    machine.pick_toppings('cheese')
    machine.pick_toppings('mayo')
    machine.pick_toppings('ketchup')
    before_inprog_lst_length = len(machine.inprogress_burger)
    try:
        machine.pick_toppings('tomato')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(before_inprog_lst_length == len(machine.inprogress_burger))
## hip2 and 03/20/23 Description: The above test case makes a burger by selecting a bun and two patties, then going next and then 3 toppings, with a maximum limit of three topping per order as 
# number of max topping are initialized to 3 in burgermachine.py. After that, I'm calculating the length of the in-progress burger, and in the try except block, I'm adding the 
# fourth topping. If we get the ExceededRemainingChoicesException, the test case is successful.


def test_6_calculate_cost(machine):
    count = 0
    while count < 4:
        bun = random.randrange(0, 4, 1)
        pat = random.randrange(0, 3, 1)
        top = random.randrange(0, 8, 1)
        random_burger = [machine.buns[bun],machine.patties[pat],machine.toppings[top]]
        random_burger_price = random_burger[0].cost + random_burger[1].cost + random_burger[2].cost
        machine.inprogress_burger = random_burger
        original_price = machine.calculate_cost()
        assert(original_price==random_burger_price)
        count = count + 1
## hip2 and 03/20/23 Description: The above test case makes a burger out of random items. For this, I used a while loop and a random package that picks a value on its own. I am calculating the 
# cost of the burger which is made by combining the costs of all its randomly selected items and then comparing the calculated cost to the real cost.

def test_7_total_sales(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty('next')
    machine.handle_toppings("lettuce")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(3.75,'3.75')
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("veggie")
    machine.handle_patty("next")
    machine.handle_toppings('cheese')
    machine.handle_toppings('bbq')
    machine.handle_toppings("done")
    machine.handle_pay(3.5,'3.5')
    machine.handle_bun("no Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("mustard")
    machine.handle_toppings("mustard")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    machine.handle_pay(1.75,'1.75')
    expected_total_sales = 3.75 + 3.5 + 1.75
    assert(expected_total_sales == machine.total_sales)
## hip2 and 03/20/23 Description: This test case is making three burgers and calculating the projected cost before comparing it to the actual cost.


def test_8_burger_increment(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("beef")
    machine.handle_patty('next')
    machine.handle_toppings("lettuce")
    machine.handle_toppings("lettuce")
    machine.handle_toppings("mayo")
    machine.handle_toppings("done")
    machine.handle_pay(2.75,'2.75')
    machine.handle_bun("Wheat Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings('cheese')
    machine.handle_toppings('bbq')
    machine.handle_toppings("done")
    machine.handle_pay(3.5,'3.5')
    machine.handle_bun("no Bun")
    machine.handle_patty("Beef")
    machine.handle_patty("next")
    machine.handle_toppings("mustard")
    machine.handle_toppings("mustard")
    machine.handle_toppings("cheese")
    machine.handle_toppings("done")
    machine.handle_pay(1.75,'1.75')
    machine.handle_bun('wheat burger bun')
    machine.handle_patty('beef')
    machine.handle_patty('next')
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    machine.handle_pay(2.25,'2.25')
    expected_total_burgers = 4
    assert(expected_total_burgers==machine.total_burgers)