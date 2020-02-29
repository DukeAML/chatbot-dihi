# Issues

In general, every configuration and code change should be tracked as an [issue](https://gitlab.oit.duke.edu/dukeinnovate/rfa2019/chatbot-moderator/issues) in the [Gitlab repository](https://gitlab.oit.duke.edu/dukeinnovate/rfa2019/chatbot-moderator). All issues should be tagged with one or more of the following labels:

* bug, for issues that are bugs or negatively impact performance or stability;
* client, for issues relating to the client component of the solution;
* enhancement, for new features or changes to existing features;
* proposed, for changes that have been proposed but have not been vetted or approved;
* server, for issues relating to the server component of the solution;
* task, for developer tasks or actions that are not suitable to be included in the [changelog](#the-changelog);
* wont-fix, for issues that will not be fixed.

# Releases

All components of this project are versioned using [semantic versioning](https://semver.org/) in lockstep (eg, the client and server will always have the same version tag.) When creating a new release you should do the following:

1. Ensure that the [CHANGELOG](CHANGELOG.md) is up to date.
2. Tag the existing release as `releases/a.b.c`.
3. Commit and push your changes.

# The CHANGELOG

The changelog describes the notable changes for each version of the project. All changes should be grouped into one of the following categories:

`Added` for new features.
`Changed` for changes in existing functionality.
`Removed` for now removed features.
`Fixed` for any bug fixes.
`Security` in case of vulnerabilities.

Refer to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) for additional details.


## What warrants a changelog entry?

As described in the [Gitlab Docs](https://docs.gitlab.com/ee/development/changelog.html):

* Any user-facing change *should* have a changelog entry. Example: “GitLab now uses system fonts for all text.”
* A fix for a regression introduced and then fixed in the same release (i.e., fixing a bug introduced during a monthly release candidate) *should not* have a changelog entry.
* Any developer-facing change (e.g., refactoring, technical debt remediation, test suite changes) **should not** have a changelog entry. Example: “Reduce database records created during Cycle Analytics model spec.”
* Performance improvements **should** have a changelog entry.
* Any change that introduces a database migration **must** have a changelog entry.

## How to generate changelog entries

To generate the CHANGELOG from Gitlab Issues, you can leverage the script create by [Samuel Michaud](https://medium.com/@SamuelMichaud/generate-a-changelog-from-gitlabs-issue-tracker-9eced2610718) as a starting point. To use this script, open the Developer Tools while signed in to Gitlab and paste the following into the Console. The Gitlab project id (15328) will not need to be changed but the module label ("0.2.0" below) will need to be updated to reflect the version you want to pull from. After running it, copy its output from your browser and paste it into the CHANGELOG, **taking care to match the existing format**.

```
await (async (projectId, milestone) => {
    const negate = func => item => !func(item)
    const printIssue = (issue) => '* ' + issue.title + ' #' + issue.iid
    const isIssueHasLabel = (labelsToFind) => ({ labels }) => labelsToFind.some((label) => labels.join(' | ').includes(label))
    const resp = await fetch(`https://gitlab.oit.duke.edu/api/v4/projects/${projectId}/issues?scope=all&per_page=100&milestone=${milestone}&order_by=updated_at`, {credentials: 'include'})
    const data = await resp.json()

    const changelog = [];
    const bugs = data.filter(isIssueHasLabel(['bug', ]))
    const refacto = data.filter(isIssueHasLabel(['task',]))
    const others = data.filter(negate(isIssueHasLabel(['bug', 'task','wont-fix'])))

    changelog.push('## 🔥 Features  ')
    changelog.push(...others.map(printIssue))

    changelog.push('\n\n## 🚀 Refacto/Optimisation  ')
    changelog.push(...refacto.map(printIssue))

    changelog.push('\n\n## 🐞 Fix  ')
    changelog.push(...bugs.map(printIssue))

    return changelog.join('\n')
})('15328', '0.2.0')
```