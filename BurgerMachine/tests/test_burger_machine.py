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
    previous_inprog_burger = len(machine.inprogress_burger)
    try:
        machine.pick_patty('turkey')
        machine.pick_toppings('mustard')
    except InvalidStageException:
        assert(True)
    finally:
        assert(previous_inprog_burger == len(machine.inprogress_burger))
#kb97 | 03/27/23 | This test case method counts the length of the inprogress burger then adds patty and toppings in the try block, since patty and toppings can not 
# be added until a selection of bun is made, it's going in exception state ie.InvalidStageException and in finally the len of inprogress burger(previous one we counted in 
# beginning) is matched with current's inprogress burger length in assert so the test case will work if only those two matched. 

def test2_patty_in_stock(machine):
    machine.patties[0].quantity = 0
    name = machine.patties[0].name.lower()
    machine.handle_bun('wheat burger bun')
    previous_inprog_burger = len(machine.inprogress_burger)
    #machine.currently_selecting = BurgerMachine.STAGE.patties
    try:
        machine.pick_patty(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(previous_inprog_burger == len(machine.inprogress_burger))   
#kb97 | 03/27/23 | This test case checks if patty is in stock or not, so I intialized one of the patties amount to zero, turkey in this case and then tried running the machine
# with the nromal selection flow and selecting turkey as my patty, since the patty is out of stock, the OutofStockException will be triggered and the test case will pass.

def test3_topping_in_stock(machine):
    machine.toppings[2].quantity = 0
    name = machine.toppings[2].name.lower()
    machine.handle_bun('white burger bun')
    machine.handle_patty('beef')
    machine.handle_patty('veggie')
    machine.handle_patty('next')
    previous_inprog_burger = len(machine.inprogress_burger)
    try:
        machine.pick_toppings(name)
    except OutOfStockException:
        assert(True)
    finally:
        assert(previous_inprog_burger == len(machine.inprogress_burger))
#kb97 | 03/27/23 | This test case checks if a topping is in stock or not, so I intialized one of the toppings amount to zero, tomato in this case and then tried running the machine
# with the normal selection flow (bun first then a patty) and selecting tomato as my topping, since the topping is out of stock, the OutofStockException will be triggered and the test case will pass.

        
def test4_add_3_patties(machine):
    machine.handle_bun('lettuce wrap')
    machine.pick_patty('veggie')
    machine.pick_patty('beef')
    machine.pick_patty('beef')
    previous_inprog_burger = len(machine.inprogress_burger)
    try:
        machine.pick_patty('veggie')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(previous_inprog_burger == len(machine.inprogress_burger))
#kb97 | 03/27/23 |The test case makes a burger by selecting a bun and three patties, with a maximum limit of three patties per order as number of max patties are initialized to 3 in burgermachine.py
#In the try except block, I will add the 4th patty, since the max. number of patties are 3, we get the ExceededRemainingChoicesException, 
# the test case passes


def test5_add_3_toppings(machine):
    machine.handle_bun('wheat burger bun')
    machine.handle_patty('beef')
    machine.handle_patty('veggie')
    machine.handle_patty('next')
    machine.pick_toppings('mustard')
    machine.pick_toppings('tomato')
    machine.pick_toppings('bbq')
    previous_inprog_burger = len(machine.inprogress_burger)
    try:
        machine.pick_toppings('tomato')
    except ExceededRemainingChoicesException:
        assert(True)
    finally:
        assert(previous_inprog_burger == len(machine.inprogress_burger))
#kb97 | 03/27/23 |The test case makes a burger by selecting a bun and two patties, and then 3 toppings, with a maximum limit of three toppings per order as number of max toppings are initialized to 3
#I will try to add a 4th topping in the try block, but since the max. number of toppings are 3, we get the ExceededRemainingChoicesException, 
# the test case passes


def test6_calculate_cost(machine):
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
#kb97 | 03/27/23 | The above test case makes a burger out of random items. I used a while loop and a random package that picks a value randomly on its own. I am calculating the 
# cost of the burger which is made by combining the costs of all its randomly selected items and then comparing the calculated cost to the real cost.

def test7_total_sales(machine):
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty('next')
    machine.handle_toppings("lettuce")
    machine.handle_toppings("bbq")
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
#kb97 | 03/27/23 | This test case is making three burgers and calculating the projected cost before comparing it to the actual cost.


def test8_burger_increment(machine):
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