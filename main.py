from robotics import Robot

SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Marie Curie", "Charles Darwin"]

robot = Robot("Quandrinaut")


def introduce_yourself():
    robot.say_hello()


def main():
    introduce_yourself()
    print("\n")
    robot.robo_steps()
    print("\n")
    for scientist in SCIENTISTS:
            information1, information2, information3, information4,age = robot.scientist_info(scientist)
            robot.display_information(information1, information2, information3, information4,age)
    print("\n")
    robot.new_search()
    print("\n")
    robot.cleanup()


if __name__ == "__main__":
    main()
