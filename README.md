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

The test deployment is on https://dev-www.materialscloud.org/work/tools/optimadeclient, the production deployment is on https://www.materialscloud.org/work/tools/optimadeclient. 
Both use the same database providers list retrieved from https://aiida.materialscloud.org/optimade/v1/links

## Contacts

Casper Welzel Andersen, casper.andersen@epfl.ch
Jusong Yu, jusong.yu@epfl.ch
Kristjan Eimre, kristjan.eimre@epfl.ch 