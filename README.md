# OPTIMADE Client

An OPTIMADE Client as a Materials Cloud tool.

It runs a Jupyter notebook in Voilà with the [Materials Cloud Voilà template](https://github.com/materialscloud-org/voila-materialscloud-template).

## Test and deploy

Once the changes are make, push to `dev-dokku` server to see if the new changes work well by running: 

```bash
git remote add dev-dokku dokku@matcloud.xyz:optimadeclient
git push dev-dokku <local-test-branch>:master
```

If all good after merge the PR to `master` branch, the deploy CI action will automatically run push to production `dokku` server.

## Authors

Casper Welzel Andersen, casper.andersen@epfl.ch
