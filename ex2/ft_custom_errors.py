#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(plant_status: str) -> None:
    if plant_status == "wilting":
        raise PlantError("The tomato plant is wilting!")
    print("Plant is healthy.")


def check_water(water_level: int) -> None:
    if water_level < 5:
        raise WaterError("Not enough water in the tank!")
    print("Water level is fine")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        check_plant("wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    try:
        print("\nTesting WaterError...")
        check_water(4)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")

    try:
        check_plant("wilting")
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        check_water(4)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
