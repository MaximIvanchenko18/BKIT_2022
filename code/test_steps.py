from behave import given, when, then, step
from main2 import Unique


@given('we have list of integers [{arr}]')
def step(context, arr):
    context.data = [int(elem) for elem in arr.split(', ')]


@given('we have generator [{gen}]')
def step(context, gen):
    context.data = (int(elem) for elem in gen.split(', '))


@given('we have list of strings [{arr}]')
def step(context, arr):
    context.data = arr.split(', ')


@when('we run Unique() iterator')
def step(context):
    context.res = list(Unique(context.data))


@when('we run Unique() iterator with ignore_case')
def step(context):
    context.res = list(Unique(context.data, ignore_case=True))


@then('we get values without repetition [{arr}]')
def step(context, arr):
    assert context.res == [int(elem) for elem in arr.split(', ')]


@then('we get symbols without repetition [{arr}]')
def step(context, arr):
    assert sorted(context.res) == sorted(arr.split(', '))
