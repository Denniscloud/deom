from pandas.core.arrays.categorical import Categorical as Categorical  # , CategoricalDtype as CategoricalDtype

def recode_for_groupby(c: Categorical, sort: bool, observed: bool): ...
def recode_from_groupby(c: Categorical, sort: bool, ci): ...
