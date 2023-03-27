from enum import Enum
import sys
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, NeedsCleaningException, OutOfStockException
from BurgerMachineExceptions import InvalidPaymentException

class Usable:
    name = ""
    quantity = 0
    cost = 99

    def __init__(self, name, quantity = 10, cost=99):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def use(self):
        self.quantity -= 1
        if (self.quantity < 0):
            raise OutOfStockException
        return self.quantity 

    def in_stock(self):
        return self.quantity > 0
    def __repr__(self) -> str:
        return self.name

class Bun(Usable):
    pass

class Patty(Usable):
    pass

class Topping(Usable):
    pass

class STAGE(Enum):
    Bun = 1
    Patty = 2
    Toppings = 3
    Pay = 4

class BurgerMachine:
    # Constants https://realpython.com/python-constants/
    USES_UNTIL_CLEANING = 15
    MAX_PATTIES = 3
    MAX_TOPPINGS = 3


    buns = [Bun(name="No Bun", cost=0), Bun(name="White Burger Bun", cost=1), Bun("Wheat Burger Bun", cost=1.25),Bun("Lettuce Wrap", cost=1.5)]
    patties = [Patty(name="Turkey", quantity=10, cost=1), Patty(name="Veggie", quantity=10, cost=1), Patty(name="Beef", quantity=10, cost=1)]
    toppings = [Topping(name="Lettuce", quantity=10, cost=.25), Topping(name="Tomato", quantity=10, cost=.25), Topping(name="Pickles", quantity=10, cost=.25), \
    Topping(name="Cheese", quantity=10, cost=.25), Topping(name="Ketchup", quantity=10, cost=.25),
    Topping(name="Mayo", quantity=10, cost=.25), Topping(name="Mustard", quantity=10, cost=.25),Topping(name="BBQ", quantity=10, cost=.25)] 


    # variables
    remaining_uses = USES_UNTIL_CLEANING
    remaining_patties = MAX_PATTIES
    remaining_toppings = MAX_TOPPINGS
    total_sales = 0
    total_burgers = 0

    inprogress_burger = []
    currently_selecting = STAGE.Bun

    # rules
    # 1 - bun must be chosen first
    # 2 - can only use items if there's quantity remaining
    # 3 - patties can't exceed max
    # 4 - toppings can't exceed max
    # 5 - proper cost must be calculated and shown to the user
    # 6 - cleaning must be done after certain number of uses before any more burgers can be made
    # 7 - total sales should calculate properly based on cost calculation
    # 8 - total_burgers should increment properly after a payment
    

    def pick_bun(self, choice):
        if self.currently_selecting != STAGE.Bun:
            raise InvalidStageException
        for c in self.buns:
            if c.name.lower() == choice.lower():
                c.use()
                self.inprogress_burger.append(c)
                return
        raise InvalidChoiceException

    def pick_patty(self, choice):
        if self.currently_selecting != STAGE.Patty:
            raise InvalidStageException
        if self.remaining_uses <= 0:
            raise NeedsCleaningException
        if self.remaining_patties <= 0:
            raise ExceededRemainingChoicesException
        for f in self.patties:
            if f.name.lower() == choice.lower():
                f.use()
                self.inprogress_burger.append(f)
                self.remaining_patties -= 1
                self.remaining_uses -= 1
                return
        raise InvalidChoiceException

    def pick_toppings(self, choice):
        if self.currently_selecting != STAGE.Toppings:
            raise InvalidStageException
        if self.remaining_toppings <= 0:
            raise ExceededRemainingChoicesException
        for t in self.toppings:
            if t.name.lower() == choice.lower():
                t.use()
                self.inprogress_burger.append(t)
                self.remaining_toppings -= 1
                return
        raise InvalidChoiceException

    def reset(self):
        self.remaining_patties = self.MAX_PATTIES
        self.remaining_toppings = self.MAX_TOPPINGS
        self.inprogress_burger = []
        self.currently_selecting = STAGE.Bun

    def clean_machine(self):
        self.remaining_uses = self.USES_UNTIL_CLEANING
        
    def handle_bun(self, bun):
        self.pick_bun(bun)
        self.currently_selecting = STAGE.Patty

    def handle_patty(self, patty):
        if patty == "next":
            self.currently_selecting = STAGE.Toppings
        else:
            self.pick_patty(patty)

    def handle_toppings(self, toppings):
        if toppings == "done":
            self.currently_selecting = STAGE.Pay
        else:
            self.pick_toppings(toppings)

    def handle_pay(self, expected, total):
        if self.currently_selecting != STAGE.Pay:
            raise InvalidStageException
        if total == str(expected):
            print("Thank you! Enjoy your burger!")
            self.total_burgers += 1
            self.total_sales += expected # only if successful
            #print(f"Total sales so far {self.total_sales}")
            self.reset()
        else:
            raise InvalidPaymentException
        
    def print_current_burger(self):
        print(f"Current Burger: {','.join([x.name for x in self.inprogress_burger])}")

    def calculate_cost(self):
        # TODO add the calculation expression/logic for the inprogress_burger
        #kb97 | 03/25/23 | This function sums up the cost of all items in the inprogress-burger array by addings the cost of each item. 
        #The cost_of_burger is then rounded and returned.
        cost_of_burger = 0
        for item in self.inprogress_burger:
            cost_of_burger += item.cost
        return round(cost_of_burger, 2)

    def run(self):
        try:
            if self.currently_selecting == STAGE.Bun:
                bun = input(f"What type of bun would you like {', '.join(list(map(lambda c:c.name.lower(), filter(lambda c: c.in_stock(), self.buns))))}?\n")
                self.handle_bun(bun)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Patty:
                patty = input(f"Would type of patty would you like {', '.join(list(map(lambda f:f.name.lower(), filter(lambda f: f.in_stock(), self.patties))))}? Or type next.\n")
                self.handle_patty(patty)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Toppings:
                toppings = input(f"What topping would you like {', '.join(list(map(lambda t:t.name.lower(), filter(lambda t: t.in_stock(), self.toppings))))}? Or type done.\n")
                self.handle_toppings(toppings)
                self.print_current_burger()
            elif self.currently_selecting == STAGE.Pay:
                expected = self.calculate_cost()
                # show expected value as currency format
                # require total to be entered as currency format
                total = input(f"Your total is {expected}, please enter the exact value.\n")
                self.handle_pay(expected, total)
                
                choice = input("What would you like to do? (order or quit)\n")
                if choice == "quit":
                    #exit() in recursive functions creates stackoverflow
                    # use return 1 to exit
                    print("Quitting the burger machine")
                    return 1
        except KeyboardInterrupt:
            # quit
            print("Quitting the burger machine")
            sys.exit()
        
        # handle OutOfStockException
            # show an appropriate message of what stage/category was out of stock
        except OutOfStockException as e:
            print(f"Sorry, {self.currently_selecting.name} is out of stock. Please make another selection.")
        #kb97 | 03/25/23 | This function throws an exception when a certain item (patty, topping) is out of stock, since we have define that each item has only 
        #10 units in stock, once 10 items of a particular topping or patty are used up, this will prompt the user that item is out of stock.   
            
        # handle NeedsCleaningException
            # prompt user to type "clean" to trigger clean_machine()
            # any other input is ignored
            # print a message whether or not the machine was cleaned
        except NeedsCleaningException as e:
            clean = input("The machine needs cleaning. Type 'clean' to clean or any other key to ignore.\n")
            if clean.lower() == "clean":
                self.clean_machine()
                print("The machine has been cleaned.")
            else:
                print("The machine was not cleaned, enter proper input to clean it.")
        #kb97 | 03/26/23 | This function cleans the burger machine by prompting the user to enter the word 'clean', if machine is cleaned,
        # a message showing success will be printed, and a message showing failure if it failed to clean

        # handle InvalidChoiceException
            # show an appropriate message of what stage/category was the invalid choice was in
            # show an appropriate message of what stage/category was the invalid choice was in
        except InvalidChoiceException as e:
            print(f"Sorry, The option you selected is not a valid choice in {self.currently_selecting.name}.")
        #kb97 | 03/26/23 | This function will throw an exception if there is an invalid choice being made, for example, toppings are being entred when a bun or patty is being expected

        # handle ExceededRemainingChoicesException
            # show an appropriate message of which stage/category was exceeded
            # move to the next stage/category
        except ExceededRemainingChoicesException as e:
            print(f"Sorry, you have exceeded the remaining choices in {self.currently_selecting.name}.")
            if(self.currently_selecting == STAGE.Bun):
                self.currently_selecting = STAGE.Patty
            elif(self.currently_selecting == STAGE.Patty):
                self.currently_selecting = STAGE.Toppings
            else:
                self.currently_selecting = STAGE.Pay    
        #kb97 | 03/26/23 | This function will throw an exception if more than 3 toppings or patties are selected, as the max selection limit for these things is 3.


        # handle InvalidPaymentException
            # show an appropriate message
        except InvalidPaymentException as e:
            print(f"Sorry, your payment  is invalid.")
        #kb97 | 03/26/23 | This execption happens when the exact amount indiciated on the screen is not input.    

        except:
            # this is a default catch all, follow the steps above
            print("Something went wrong")
        
        self.run()

    def start(self):
        self.run()

    
if __name__ == "__main__":
    bm = BurgerMachine()
    bm.start()