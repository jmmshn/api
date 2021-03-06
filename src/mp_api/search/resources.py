from mp_api.core.resource import Resource
from mp_api.search.models import SearchDoc

from mp_api.core.query_operator import PaginationQuery, SortQuery, SparseFieldsQuery
from mp_api.materials.query_operators import (
    FormulaQuery,
    MinMaxQuery,
    SymmetryQuery,
    DeprecationQuery,
)
from mp_api.elasticity.query_operators import (
    BulkModulusQuery,
    ShearModulusQuery,
    PoissonQuery,
)
from mp_api.dielectric.query_operators import DielectricQuery
from mp_api.piezo.query_operators import PiezoelectricQuery
from mp_api.surface_properties.query_operators import SurfaceMinMaxQuery
from mp_api.search.query_operators import (
    SearchBandGapQuery,
    HasPropsQuery,
    ThermoEnergySearchQuery,
    SearchTaskIDsQuery,
    SearchIsStableQuery,
)


def search_resource(eos_store):
    resource = Resource(
        eos_store,
        SearchDoc,
        query_operators=[
            FormulaQuery(),
            MinMaxQuery(),
            SymmetryQuery(),
            ThermoEnergySearchQuery(),
            SearchIsStableQuery(),
            SearchBandGapQuery(),
            BulkModulusQuery(),
            ShearModulusQuery(),
            PoissonQuery(),
            DielectricQuery(),
            PiezoelectricQuery(),
            SurfaceMinMaxQuery(),
            SearchTaskIDsQuery(),
            HasPropsQuery(),
            DeprecationQuery(),
            SortQuery(),
            PaginationQuery(),
            SparseFieldsQuery(SearchDoc, default_fields=["task_id"]),
        ],
        tags=["Search"],
    )

    return resource
