db.createUser(
    {
        user: "helpdev",
        pwd: "123456",
        roles: [
            {
                role: "readWrite",
                db: "bank"
            }
        ]
    }
);

db = db.getSiblingDB('bank');
db.createCollection('sample');

//db.sample.insertMany(data);