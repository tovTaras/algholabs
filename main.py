from math import sqrt


def find_length_of_cable(distance: int, pylons: list[int]):
    length: float = 0
    if len(pylons) <= 50:
        suitable: bool = True
        for pylon_height in pylons:
            if pylon_height < 1 or pylon_height > 100:
                suitable = False
                break
        if suitable:
            is_last_was_changed_to_one: bool = False
            index: int = 0
            for pylon_height in pylons:
                index += 1
                if index != len(pylons):
                    if is_last_was_changed_to_one:
                        if pylons[index] > 1:
                            length += sqrt((pylons[index] - 1)**2 + distance**2)
                        else:
                            length += distance
                        is_last_was_changed_to_one = False
                    else:
                        with_no_changes: float = sqrt((pylons[index] - pylon_height)**2 + distance**2)
                        with_changes: float = sqrt((1 - pylon_height)**2 + distance**2)
                        if with_changes > with_no_changes:
                            is_last_was_changed_to_one = True
                            length += with_changes
                        else:
                            length += with_no_changes
        else:
            print("Elements must be in limit between 1 to 100")
    else:
        print("List is longer than 50 elements")

    print(f'We need to purchase {round(length, 2)} m of cable, for the worst scenario')


def main():
    with open("input.txt", 'r') as r:
        distance_between_pylons: int = int(r.readline())
        heights: list[int] = list(map(int, r.readline().split()))
        find_length_of_cable(distance_between_pylons, heights)


if __name__ == '__main__':
    main()