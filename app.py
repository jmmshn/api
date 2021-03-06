import os
from monty.serialization import loadfn
from mp_api.core.api import MAPI
from mp_api.materials.resources import materials_resource
from mp_api.tasks.resources import task_resource
from mp_api.tasks.resources import task_deprecation_resource
from mp_api.tasks.resources import trajectory_resource
from mp_api.thermo.resources import thermo_resource
from mp_api.dielectric.resources import dielectric_resource
from mp_api.magnetism.resources import magnetism_resource
from mp_api.piezo.resources import piezo_resource
from mp_api.phonon.resources import phonon_bs_resource, phonon_img_resource
from mp_api.eos.resources import eos_resource
from mp_api.similarity.resources import similarity_resource
from mp_api.xas.resources import xas_resource
from mp_api.gb.resources import gb_resource
from mp_api.fermi.resources import fermi_resource
from mp_api.elasticity.resources import elasticity_resource
from mp_api.dois.resources import dois_resource
from mp_api.substrates.resources import substrates_resource
from mp_api.surface_properties.resources import surface_props_resource
from mp_api.wulff.resources import wulff_resource
from mp_api.robocrys.resources import robo_resource
from mp_api.synthesis.resources import synth_resource
from mp_api.electrodes.resources import insertion_electrodes_resource
from mp_api.molecules.resources import molecules_resource
from mp_api.charge_density.resources import charge_density_resource
from mp_api.search.resources import search_resource
from mp_api.bandstructure.resources import bs_resource
from mp_api.dos.resources import dos_resource


resources = {}

db_uri = os.environ.get("MPCONTRIBS_MONGO_HOST", None)
db_version = os.environ.get("DB_VERSION")

# Uncomment to use JSON store for development
# core_store = JSONStore("./test_files/materials_Li_Fe_V.json")
# task_store = JSONStore("./test_files/tasks_Li_Fe_V.json")

materials_store_json = os.environ.get("MATERIALS_STORE", "materials_store.json")
task_store_json = os.environ.get("TASK_STORE", "task_store.json")
thermo_store_json = os.environ.get("THERMO_STORE", "thermo_store.json")
dielectric_piezo_store_json = os.environ.get(
    "DIELECTRIC_PIEZO_STORE", "dielectric_piezo_store.json"
)
magnetism_store_json = os.environ.get("MAGNETISM_STORE", "magnetism_store.json")
phonon_bs_store_json = os.environ.get("PHONON_BS_STORE", "phonon_bs_store.json")
phonon_img_store_json = os.environ.get("PHONON_IMG_STORE", "phonon_img_store.json")
eos_store_json = os.environ.get("EOS_STORE", "eos_store.json")
similarity_store_json = os.environ.get("SIMILARITY_STORE", "similarity_store.json")
xas_store_json = os.environ.get("XAS_STORE", "xas_store.json")
gb_store_json = os.environ.get("GB_STORE", "xas_store.json")
fermi_store_json = os.environ.get("FERMI_STORE", "fermi_store.json")
elasticity_store_json = os.environ.get("ELASTICITY_STORE", "elasticity_store.json")
doi_store_json = os.environ.get("DOI_STORE", "doi_store.json")
substrates_store_json = os.environ.get("SUBSTRATES_STORE", "substrates_store.json")
surface_props_store_json = os.environ.get(
    "SURFACE_PROPS_STORE", "surface_props_store.json"
)
wulff_store_json = os.environ.get("WULFF_STORE", "wulff_store.json")
robocrys_store_json = os.environ.get("ROBOCRYS_STORE", "robocrys_store.json")
synth_store_json = os.environ.get("SYNTH_STORE", "synth_store.json")
insertion_electrodes_store_json = os.environ.get(
    "INSERTION_ELECTRODES_STORE", "insertion_electrodes_store.json"
)
molecules_store_json = os.environ.get("MOLECULES_STORE", "molecules_store.json")
search_store_json = os.environ.get("SEARCH_STORE", "search_store.json")

bs_store_json = os.environ.get("BS_STORE", "bs_store.json")
dos_store_json = os.environ.get("DOS_STORE", "dos_store.json")

s3_bs_index_json = os.environ.get("S3_BS_INDEX_STORE", "s3_bs_index.json")
s3_dos_index_json = os.environ.get("S3_DOS_INDEX_STORE", "s3_dos_index.json")

s3_bs_json = os.environ.get("S3_BS_STORE", "s3_bs.json")
s3_dos_json = os.environ.get("S3_DOS_STORE", "s3_dos.json")

s3_chgcar_index_json = os.environ.get("CHGCAR_INDEX_STORE", "chgcar_index_store.json")
s3_chgcar_json = os.environ.get("S3_CHGCAR_STORE", "s3_chgcar.json")


if db_uri:
    from maggma.stores import MongoURIStore, S3Store

    materials_store = MongoURIStore(
        uri=f"mongodb+srv://{db_uri}",
        database="mp_core",
        key="task_id",
        collection_name=f"materials.core_{db_version}",
    )

    task_store = MongoURIStore(
        uri=f"mongodb+srv://{db_uri}",
        database="mp_core",
        key="task_id",
        collection_name="tasks",
    )

    thermo_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name=f"thermo_{db_version}",
    )

    dielectric_piezo_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="dielectric",
    )

    magnetism_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="magnetism",
    )

    phonon_bs_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="phonon_bs",
    )

    phonon_img_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="phonon_img",
    )

    eos_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="eos",)

    similarity_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="similarity",
    )

    xas_store = MongoURIStore(uri=db_uri, key="xas_id", collection_name="xas",)

    gb_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="grain_boundaries",
    )

    fermi_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="fermi_surface",
    )

    elasticity_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="elasticity",
    )

    doi_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="dois",)

    substrates_store = MongoURIStore(
        uri=db_uri, key="film_id", collection_name="substrates",
    )

    surface_props_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="surface_properties",
    )

    wulff_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="wulff",)

    robo_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="robocrys",)

    synth_store = MongoURIStore(
        uri=db_uri, key="_id", collection_name="synth_descriptions",
    )

    insertion_electrodes_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="insertion_electrodes",
    )

    molecules_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="molecules",
    )

    search_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="search",)

    bs_store = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="bandstructure",
    )

    s3_bs_index = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="s3_bandstructure_index",
    )

    dos_store = MongoURIStore(uri=db_uri, key="task_id", collection_name="dos",)

    s3_dos_index = MongoURIStore(
        uri=db_uri, key="task_id", collection_name="s3_dos_index",
    )

    s3_bs = S3Store(index=s3_bs_index, bucket="mp-bandstructures", compress=True)

    s3_dos = S3Store(index=s3_dos_index, bucket="mp-dos", compress=True)

    s3_chgcar_index = MongoURIStore(
        uri=db_uri,
        database="mp_core",
        key="fs_id",
        collection_name="atomate_chgcar_fs_index",
    )

    s3_chgcar = S3Store(
        index=s3_chgcar_index,
        bucket="mp-volumetric",
        sub_dir="atomate_chgcar_fs/",
        compress=False,
        key="fs_id",
        searchable_fields=["task_id", "fs_id"],
    )


else:
    materials_store = loadfn(materials_store_json)
    task_store = loadfn(task_store_json)
    thermo_store = loadfn(thermo_store_json)
    dielectric_piezo_store = loadfn(dielectric_piezo_store_json)
    magnetism_store = loadfn(magnetism_store_json)
    phonon_bs_store = loadfn(phonon_bs_store_json)
    phonon_img_store = loadfn(phonon_img_store_json)
    eos_store = loadfn(eos_store_json)
    similarity_store = loadfn(similarity_store_json)
    xas_store = loadfn(xas_store_json)
    gb_store = loadfn(gb_store_json)
    fermi_store = loadfn(fermi_store_json)
    elasticity_store = loadfn(elasticity_store_json)
    doi_store = loadfn(doi_store_json)
    substrates_store = loadfn(substrates_store_json)
    surface_props_store = loadfn(surface_props_store_json)
    wulff_store = loadfn(wulff_store_json)
    robo_store = loadfn(robocrys_store_json)
    synth_store = loadfn(synth_store_json)
    insertion_electrodes_store = loadfn(insertion_electrodes_store_json)
    molecules_store = loadfn(molecules_store_json)
    search_store = loadfn(search_store_json)

    bs_store = loadfn(bs_store_json)
    dos_store = loadfn(dos_store_json)
    s3_bs_index = loadfn(s3_bs_index_json)
    s3_dos_index = loadfn(s3_dos_index_json)
    s3_bs = loadfn(s3_bs_json)
    s3_dos = loadfn(s3_dos_json)

    s3_chgcar_index = loadfn(s3_chgcar_index_json)
    s3_chgcar = loadfn(s3_chgcar_json)

# Materials
resources.update({"materials": materials_resource(materials_store)})

# Tasks
resources.update({"tasks": task_resource(task_store)})

# Task Deprecation
resources.update({"deprecation": task_deprecation_resource(materials_store)})

# Trajectory
resources.update({"trajectory": trajectory_resource(task_store)})

# Thermo
resources.update({"thermo": thermo_resource(thermo_store)})

# Dielectric
resources.update({"dielectric": dielectric_resource(dielectric_piezo_store)})

# Magnetism
resources.update({"magnetism": magnetism_resource(magnetism_store)})

# Piezoelectric
resources.update({"piezoelectric": piezo_resource(dielectric_piezo_store)})

# Phonon
resources.update({"phonon": phonon_bs_resource(phonon_bs_store)})
resources.update({"phonon_img": phonon_img_resource(phonon_img_store)})

# EOS
resources.update({"eos": eos_resource(eos_store)})

# Similarity
resources.update({"similarity": similarity_resource(similarity_store)})

# XAS
resources.update({"xas": xas_resource(xas_store)})

# Grain Boundaries
resources.update({"gb": gb_resource(gb_store)})

# Fermi Surface
resources.update({"fermi": fermi_resource(fermi_store)})

# Elasticity
resources.update({"elasticity": elasticity_resource(elasticity_store)})

# DOIs
resources.update({"doi": dois_resource(doi_store)})

# Substrates
resources.update({"substrates": substrates_resource(substrates_store)})

# Surface Properties
resources.update({"surface_properties": surface_props_resource(surface_props_store)})

# Wulff
resources.update({"wulff": wulff_resource(wulff_store)})

# Robocrystallographer
resources.update({"robocrys": robo_resource(robo_store)})

# Synthesis
resources.update({"synthesis": synth_resource(synth_store)})

# Electrodes
resources.update(
    {"insertion_electrodes": insertion_electrodes_resource(insertion_electrodes_store)}
)

# Molecules
resources.update({"molecules": molecules_resource(molecules_store)})

# Charge Density
resources.update({"charge_density": charge_density_resource(s3_chgcar)})

# Search
resources.update({"search": search_resource(search_store)})

# Band Structure
resources.update({"bs": bs_resource(bs_store, s3_bs)})

# DOS
resources.update({"dos": dos_resource(dos_store, s3_dos)})

api = MAPI(resources=resources)
app = api.app
