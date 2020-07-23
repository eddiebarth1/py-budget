import argparse
import logging
import os
import sys
import pprint

from pprint import pformat


# Let's set up some logging here!
log_format = "%(asctime)s | %(levelname)-7s | " \
                "%(filename)s:%(lineno)d | %(processName)s | %(message)s"

main_logger = logging.getLogger(__name__)

main_log_handler = logging.StreamHandler(sys.stdout)
main_log_handler.setLevel(logging.DEBUG)

def paycheck_retrieve():

    paycheck = input("Please enter your paycheck amount: \n")
    paycheck = float(paycheck)
    print ("You entered: ${} \n".format(paycheck))

    return paycheck


def define_bills():
    bills_total = 0
    bills_dict = {}

    bills_add = True

    while bills_add:
        new_retrieve = input("Please enter the name of the bill and its amount," + \
                "separated by a comma. \n")
        print ("You entered: {}".format(new_retrieve))
        tmp_list = new_retrieve.split(",")
        bill_key = tmp_list[0]
        bill_val = tmp_list[1]

        bills_dict[bill_key] = float(bill_val)

        print ("Your current list of bills and amounts is: \n ")
        print ("{" + "\n".join("{} : {}".format(key, value) for key, value in bills_dict.items()) + "}")

        new_confirm = input("Do you have any other bills to add? Enter y or n to proceed. \n")

        if new_confirm.lower() == "n":
            for amt in bills_dict.values():
                bills_total += amt

            print ("The total cost of your bills is: ${}".format(bills_total))

            bills_add = False

        elif new_confirm.lower() == "y":
            continue

        else:
            print ("That is an incorrect response.  Exiting. \n")
            for amt in bills_dict.values():
                bills_total += amt

            break

    return bills_total


def read_expenses(expense_file):
    recurring_expenses = {}
    tmp_list = []

    with open(expense_file, 'r') as file:
        for line in file:
            line.lstrip()
            line.rstrip()
            tmp_list.append(line)

        file.close()

    main_logger.info("From the Expense file, we extracted: ---- {}".format(pformat(tmp_list)))
    for expense in tmp_list:
        main_logger.info("New Expense: ---- {}".format(expense))
        new_exp = expense.split(",")
        recurring_expenses[new_exp[0]] = float(new_exp[1])
        main_logger.debug("Recurring Expenses Updated: ---- {}".format(pformat(recurring_expenses)))

    return recurring_expenses


def main():

    logging.basicConfig(
        filename="/var/log/py-budgeting.log",
        level=logging.INFO,
        format=log_format
    )

    parser = argparse.ArgumentParser(
        description="""
            This short program will give you the difference between
            your total bill costs and whatever paycheck value you define
            You may pass various options to streamline entering info.
            """
        )

    parser.add_argument(
        '--debug',
        help='Enable debug logging',
        default=None
        )

    parser.add_argument(
        '-f',
        '--exp_file',
        help=(
            'Input file of expenses, in format:' + '<expense_name>,<amt> -- with each new expense on a new line.'
            ),
        default=None
        )

    parser.add_argument(
        '-p',
        '--paycheck',
        help='Input paycheck amount sooner rather than later. ',
        default=None
        )

    args = parser.parse_args()

    if args.debug:
        main_logger.setLevel(logging.DEBUG)
        main_logger.addHandler(main_log_handler)

    if not args.paycheck:
        args.paycheck = paycheck_retrieve()

    if not args.exp_file:
        bills_total = define_bills()

    elif args.exp_file:
        bills_dict = read_expenses(args.exp_file)
        bills_total = 0
        for amt in bills_dict.values():
            bills_total += amt

    paycheck = float(args.paycheck)

    print ("\nTotal pay for this period is: ${} \n".format(paycheck))
    print ("Your expenses for this period are: \n")
    pprint.pprint(bills_dict)
    print ("\n Total bill payments = ${} \n".format(round(bills_total, 2)))

    avail_bal = round(paycheck - bills_total, 2)

    print ("Your remaining balance after bills will be: {} \n".format(round(avail_bal, 2)))


if __name__ == "__main__":
    main()
