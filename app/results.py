"""Generate queries.  Not implemented, except as sample output"""
from sqlalchemy import and_
from sqlalchemy.orm import aliased
from app import db
from app.models import Pokemon, Property


# pylint: disable=unused-argument
def query_generator(attribute_array, filter_array=None, sort_array=None):
    """Generate SQLAlchemy query based on attributes and filter, sorted

    Development timed out on this.  The sample_query below is a cut and paste
    'result' from the approach intended here.
        - aliased objects would be sequentially created and used
        - query on each alias would be a combination of
            - 'root' join, currently hard-coded as pokemon_id = Pokemon.id
            - the 'query' join conditions
        - query output would be, in 'order', the 'label'd columns,
        - the query would then be 'filter'ed and 'sort'ed
        
    Sample attribute_array, for two columns in the sample_query below:
    attribute_array = [
        {"label": "name", "order": 4, "query": {"key_1": "height"}},
        {
            "label": "Abilities",
            "order": 6,
            "query": {
                "key_1": "abilities",
                "key_3": "ability",
                "key_4": "name",
            },
            "aggregate_over": [
                "key_2",
            ],
        },
    ]
    """


def sample_query():
    """Demonstrates the output from the query generator, should never be seen"""
    property_1 = aliased(Property)
    property_2 = aliased(Property)
    property_3 = aliased(Property)
    property_4 = aliased(Property)
    property_5 = aliased(Property)
    property_6 = aliased(Property)
    property_7 = aliased(Property)
    property_8 = aliased(Property)
    property_9 = aliased(Property)
    property_10 = aliased(Property)

    result_query = (
        db.session.query(  # pylint: disable=no-member
            Pokemon.name.label("name"),
            Pokemon.id.label("pokemon_id"),
            property_10.value.label("Species"),
            property_1.value.label("height"),
            property_2.value.label("sprite_url"),
            (
                property_3.value
                + ","
                + property_4.value
                + ","
                + property_5.value
                + ","
                + property_6.value
            ).label("stats"),
            (property_7.value + "," + property_8.value + "," + property_9.value).label(
                "abilities"
            ),
            # func.concat or listagg if engine supports it
            Pokemon.url.label("url"),
        )
        .outerjoin(
            property_1,
            and_(property_1.pokemon_id == Pokemon.id, property_1.key_1 == "height"),
        )
        .outerjoin(
            property_2,
            and_(
                property_2.pokemon_id == Pokemon.id,
                property_2.key_1 == "sprites",
                property_2.key_2 == "front_default",
            ),
        )
        .outerjoin(
            property_3,
            and_(
                property_3.pokemon_id == Pokemon.id,
                property_3.key_1 == "stats",
                property_3.key_2 == "1",
                property_3.key_3 == "stat",
                property_3.key_4 == "name",
            ),
        )
        .outerjoin(
            property_4,
            and_(
                property_4.pokemon_id == Pokemon.id,
                property_4.key_1 == "stats",
                property_4.key_2 == "2",
                property_4.key_3 == "stat",
                property_4.key_4 == "name",
            ),
        )
        .outerjoin(
            property_5,
            and_(
                property_5.pokemon_id == Pokemon.id,
                property_5.key_1 == "stats",
                property_5.key_2 == "3",
                property_5.key_3 == "stat",
                property_5.key_4 == "name",
            ),
        )
        .outerjoin(
            property_6,
            and_(
                property_6.pokemon_id == Pokemon.id,
                property_6.key_1 == "stats",
                property_6.key_2 == "4",
                property_6.key_3 == "stat",
                property_6.key_4 == "name",
            ),
        )
        .outerjoin(
            property_7,
            and_(
                property_7.pokemon_id == Pokemon.id,
                property_7.key_1 == "abilities",
                property_7.key_2 == "1",
                property_7.key_3 == "ability",
                property_7.key_4 == "name",
            ),
        )
        .outerjoin(
            property_8,
            and_(
                property_8.pokemon_id == Pokemon.id,
                property_8.key_1 == "abilities",
                property_8.key_2 == "2",
                property_8.key_3 == "ability",
                property_8.key_4 == "name",
            ),
        )
        .outerjoin(
            property_9,
            and_(
                property_9.pokemon_id == Pokemon.id,
                property_9.key_1 == "abilities",
                property_9.key_2 == "3",
                property_9.key_3 == "ability",
                property_9.key_4 == "name",
            ),
        )
        .outerjoin(
            property_10,
            and_(property_10.pokemon_id == Pokemon.id, property_10.key_1 == "species", property_10.key_2 == "name"),
        )
    )
    return result_query


if __name__ == "__main__":
    query = sample_query()
    query = Property.query
    for x in query:
        print(x.pokemon_id,x.name,x.key_1,x.key_2,x.key_3,x.key_4,x.key_5,x.key_6,x.key_7,x.value,)
