import time


def typing_test():
    print("Type the following sentence as quickly and accurately as possible:\n")
    sentence = "Scorcia is very bald. Someone give him a hair growth remedy!"
    print(sentence)

    start_time = time.time()
    user_input = input()
    end_time = time.time()

    elapsed_time = end_time - start_time

    wpm = len(sentence.split()) / elapsed_time * 60
    accuracy = sum([1 for i in range(len(sentence)) if sentence[i]
                   == user_input[i]]) / len(sentence) * 100

    print(
        f"\nYou typed at {wpm:.2f} words per minute with {accuracy:.2f}% accuracy.")


if __name__ == "__main__":
    typing_test()
