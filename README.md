# Monte Carlo Postman Collection

This a postman collection for all of Monte Carlo's public APIs. It was generated using a modified version of [Graphman](https://github.com/Escape-Technologies/graphman) which is included in this repo. Start by importing the mc_postman_collecton.json to postman.

![Screenshot of collection](https://github.com/monte-carlo-data/mc-postman/blob/main/images/postman.png "Postman")

## Regenerate Collection

To regenerate the collection from introspection run the command below, replacing the keys with your own

```bash
deno run --allow-net src/cli.ts https://api.getmontecarlo.com/graphql --id=keyhere --token=secrethere -57w1dwqR5W0YrEnIpUsrdgxzUthBe52pMF6Y3wXnY
```

## Environments 
Configure your Environment with the following two variables which can be created [here](https://getmontecarlo.com/settings/api)

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
