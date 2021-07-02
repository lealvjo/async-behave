from behave import given, then


@given(u'que eu faça get  no id "{id}"')
def step_impl(context, id):
    context.id_global.append(id)
    print(context.scenario.steps[0].name)
