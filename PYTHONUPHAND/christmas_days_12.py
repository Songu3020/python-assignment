def christmas_days_12():
    """
    Prints the lyrics for 'The Twelve Days of Christmas'.
    """    
    ordinal_days = {
        1: "first", 2: "second", 3: "third", 4: "fourth",
        5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth",
        9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth"
    }    
    gifts = {
        1: "A partridge in a pear tree.",
        2: "Two turtle doves,",
        3: "Three French hens,",
        4: "Four calling birds,",
        5: "Five golden rings!",
        6: "Six geese a-laying,",
        7: "Seven swans a-swimming,",
        8: "Eight maids a-milking,",
        9: "Nine ladies dancing,",
        10: "Ten lords a-leaping,",
        11: "Eleven pipers piping,",
        12: "Twelve drummers drumming,"    }

       for number in range(1, 13):
        
        print(f"On the {ordinal_days[number]} day of Christmas")
        print("My true love gave to me:")
        
               for counter in range(number, 0, -1):
            gift_line = gifts[counter]
                        
            if counter == 1 and number != 1:
                print(f"And {gift_line}")
            else:
            
                print(gift_line)
        
        print()
if __name__ == "__main__":
    christmas_days()

