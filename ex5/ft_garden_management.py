#!/usr/bin/env python3

class Plant:
    def __init__(self, plant_name: str, water_level: int, sunlight_hours: int):
        self.plant_name: str = plant_name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours


class GardenError(Exception):
    pass


class InvalidName(GardenError):
    pass


class InvalidWaterLevel(GardenError):
    pass


class InvalidSunlightHours(GardenError):
    pass


class TankEmptyError(GardenError):
    pass


class GardenManager:
    def __init__(self, name: str):
        self.name: str = name
        self.plants: list[Plant] = []
        self.water_tank: int = 3

    def add_plant(self, plant: Plant) -> None:
        try:
            self.check_plant_health(plant)
            self.plants += [plant]
            self.display_add(plant)
        except GardenError as e:
            print(f"Error adding plant: {e}")

    def display_add(self, plant: Plant) -> None:
        print(f"Added {plant.plant_name} successfully")

    def water_plants(self) -> None:
        try:
            if self.water_tank <= 0:
                raise TankEmptyError("Not enough water in tank")

            for plant in self.plants:
                if self.water_tank <= 0:
                    raise TankEmptyError("Not enough water in tank")

                plant.water_level += 1
                self.water_tank -= 1
                print(f"Watering {plant.plant_name} - success")

        except TankEmptyError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")

        finally:
            if self.water_tank > 0:
                print("Closing watering system (cleanup)")

    def check_plant_health(self, plant: Plant) -> None:
        if not plant.plant_name:
            raise InvalidName("Plant name cannot be empty")
        if not (1 < plant.water_level):
            raise InvalidWaterLevel(
                f"Water level {plant.water_level} is too low (min 1)"
            )
        if not (plant.water_level < 10):
            raise InvalidWaterLevel(
                f"Water level {plant.water_level} is too high (max 10)"
            )
        if not (2 < plant.sunlight_hours):
            raise InvalidSunlightHours(
                f"Sunlight hours {plant.sunlight_hours} is too low (min 2)"
            )
        if not (plant.sunlight_hours < 12):
            raise InvalidSunlightHours(
                f"Sunlight hours {plant.sunlight_hours} is too high (max 12)"
            )


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print("\nAdding plants to garden...")
    tomato = Plant("tomato", 4, 8)
    lettuce = Plant("lettuce", 2, 5)
    bad = Plant("", 3, 5)
    alice = GardenManager("Alice")

    alice.add_plant(tomato)
    alice.add_plant(lettuce)
    alice.add_plant(bad)
    print("\nWatering plants...")
    print("Opening watering system")
    alice.water_plants()

    lettuce.water_level = 15
    print("\nChecking plant health...")
    for plant in alice.plants:
        try:
            alice.check_plant_health(plant)
        except GardenError as e:
            print(f"Error checking {plant.plant_name}: {e}")
        else:
            print(
                f"{plant.plant_name}: healthy "
                f"(water: {plant.water_level}, "
                f"sun: {plant.sunlight_hours})"
            )
    print("\nTesting error recovery...")
    alice.water_tank = 0
    alice.water_plants()
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
