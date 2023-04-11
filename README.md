# Monte Carlo Postman Collection

Within this repo is a file called ```mc_postman_collection.json```.  This file is a postman collection for all of Monte Carlo's public GraphQL API endpoints (generated using [Graphman](https://github.com/Escape-Technologies/graphman)).

Start by importing the ```mc_postman_collecton.json``` to Postman.

![Screenshot of collection](https://github.com/monte-carlo-data/mc-postman/blob/main/images/postman.png "Postman")

## Regenerate Collection

We rebuild the file automatically every 30 days (on the 30th day of the month) in order to bring in new endpoints and changes.  However, if you have a need to regenerate the collection from introspection, you will need to setup [deno](https://deno.land/manual@v1.32.3/getting_started/installation) on your machine, clone the [Graphman](https://github.com/Escape-Technologies/graphman) repo, and run the command below.  Simply replace the keys with your own and update the path to the ```cli.ts``` as necessary.

```bash
deno run --allow-net --allow-read --allow-write graphman/src/cli.ts https://api.getmontecarlo.com/graphql --H="x-mcd-id:REPLACE_WITH_ID" -H="x-mcd-token:REPLACE_WITH_TOKEN" --out=mc_postman_collection.json
```

If you feel that the file should be updated in this repo immediately, outside of the 30 day schedule, please let us know!

## Environments 

[Configure your Postman Environment](https://learning.postman.com/docs/sending-requests/variables/) with the following two variables which can be created [here](https://getmontecarlo.com/settings/api)

```bash

x-mcd-id : MonteCarloId
x-mcd-token : MonteCarloToken
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
