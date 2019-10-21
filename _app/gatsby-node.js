const path = require('path')

exports.createPages = async ({ graphql, actions }) => {
  const { createPage } = actions

  const subjectPage = path.resolve('./src/templates/Subject.js')
  const result = await graphql(
    `
      {
        allMarkdownRemark(
          sort: { fields: [frontmatter___title], order: DESC }
          limit: 1000
        ) {
          edges {
            node {
              fields {
                slug
                slugPath
              }
              frontmatter {
                title
              }
            }
          }
        }
      }
    `
  )

  if (result.errors) {
    throw result.errors
  }

  // Create subject pages
  const subjects = result.data.allMarkdownRemark.edges

  subjects.forEach(subject => {
    createPage({
      path: subject.node.fields.slugPath,
      component: subjectPage,
      context: {
        slug: subject.node.fields.slug,
        slugPath: subject.node.fields.slugPath,
      },
    })
  })
}
