ci-gh-pages:
	fly --target k8s \
		set-pipeline \
			--pipeline "gh-pages" \
			--config "ci/pipelines/gh-pages.yml" \
			--load-vars-from "ci/credentials.yml"
