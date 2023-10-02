import server
import timeit

server.build_users_data()

def my_code():
    result = server.suggest_friends('Person_77')
    # print(result)

execution_time_seconds = timeit.timeit(
    stmt=my_code, # statement you want to measure
    # setup=None, # Setup before exicuting actual code
    number=1, # NUmber of times you want this code to run
    )

print("Suggest Friends executed in {} milli seconds".format(execution_time_seconds*1000))