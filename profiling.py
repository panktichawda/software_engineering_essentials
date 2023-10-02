import server
import timeit
import utils
user_data = utils.build_users_data('./users')

def my_code():
    result = user_data['user1'].suggest_friends()
    # print(result)

execution_time_seconds = timeit.timeit(
    stmt=my_code, # statement you want to measure
    # setup=None, # Setup before exicuting actual code
    number=1, # NUmber of times you want this code to run
    )

print("Suggest Friends executed in {} milli seconds".format(execution_time_seconds*1000))