
''' Model for aircraft flight'''
from pprint import pprint as pp


class Flight:
    ''' A flight with a particular aircraft '''

    def __init__(self, number, aircraft):  # initializer
        ''' object attributes '''
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))

        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))

        if not number[2:].isdigit() and int((number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))

        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for __ in rows]

    def number(self):  # instance methods
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def parse_seat(self, seat):
        '''Parse a seat designator into a valid row and seat

        Args:
            seat: A seat designator such as 12f.

        Returns:
            A tuple containing an integer and string for row and seat'''
        row_numbers, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}.".format(letter))

        row_text = seat[-1]
        try:
            row = int(row_text)
        except ValueError("Invalid seat row {}".format(row_text)):

            if row not in row_numbers:
                raise ValueError("Invalid row number {}".format(row))

        return row, letter

    def allocate_seat(self, seat, passenger):
        '''Allocate a seat to a passenger.

        Args:
            Seat: A passenger such as '12C' or 21F',
            passenger: The passenger name.

        Raises:
            ValueError: if the seat is unavailable.
        '''
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))

        self._seating[row][letter] = passenger

    def relocate_passenger(self, from_seat, to_seat):
        ''' Relocate a passenger to a different seat

        Args:
            from_seat: The existing seat designator for the
            passenger to be moved.

            to_seat: The new seat designator.
        '''
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError("No passenger to relocate in {}".format(from_seat))

        to_row, to_letter = self._parse_seat(to_seat)
        if self.seating[to_row][to_letter] is not None:
            raise ValueError("Seat {} already occupied".format(from_letter))

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return (sum(1 for s in row.values() if s is None)
                for row in self._seating
                if row is not None)


    def make_boarding_cards(self, card_printer):
        for passenger, seat, in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())


    def _passenger_seats(self):
        '''An iterable series of passenger seating allocations'''
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, "{}{}".format(row, letter))



class Aircraft:

    def __init__(self, regisration):
        self._registration = regisration

    def regitration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

class AirbusA319(Aircraft):

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDEF"



class Boeing777(Aircraft):

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        # for simplicities sake, we ignore complex
        # seating arrangement for first-class
        return range(1, 56), "ABCDEGHJK"




def make_flights():
    f = Flight("BA758", AirbusA319("G-EPT"))
    f.allocate_seat('12A', 'Gusido Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejlsberg')
    f.allocate_seat('1C', 'John McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')

    g = Flight("AF72", Boeing777("F-GSPS"))
    g.allocate_seat('55K', 'Larry Wall')
    g.allocate_seat('33G', 'Yukihero Matsumoto')
    g.allocate_seat('4B', 'Brian Kernighan')
    g.allocate_seat('4A', 'Dennis Ritchie')

    return f, g

def console_card_printer(passenger, seat, flight_number, aircraft):

    output = "| Name: {0} " \
            " Flight: {1} "\
            " Seat: {2}" \
            " Aircraft {3} " \
            " |".format(passenger, flight_number, seat, aircraft)
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, banner]
    card = '\n'.join(lines)
    print(card)
    print()




if __name__ == '__main__':
    f, g = make_flights()
    f.make_boarding_cards(console_card_printer)

    pp(f)
    a = AirbusA319('G-EZBT')
    print(a.num_seats())

    b =  Boeing777('N717SN')
    print(b.num_seats())

