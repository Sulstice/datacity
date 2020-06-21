ci-gh-pages:
	fly --target k8s \
		set-pipeline \
			--pipeline "gh-pages" \
			--config "ci/pipelines/gh-pages.yml" \
			--load-vars-from "ci/credentials.yml"

ci-us-tx-crime:
	fly --target k8s \
		set-pipeline \
			--pipeline "us-tx-crime" \
			--config "ci/pipelines/us-tx-crime.yml" \
			--load-vars-from "ci/credentials.yml"
