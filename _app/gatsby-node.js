const path = require('path')
const { createFilePath } = require('gatsby-source-filesystem')

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

exports.onCreateNode = ({ node, actions, getNode }) => {
  const { createNodeField } = actions

  if (node.internal.type === 'MarkdownRemark') {
    const value =
      node.frontmatter.slug ||
      createFilePath({ node, getNode }).replace('README/', '')

    createNodeField({
      name: 'slug',
      node,
      value: value,
    })

    createNodeField({
      name: 'slugPath',
      node,
      value: value.replace(/([A-Z])/g, (_, v) => '-' + v.toLowerCase()),
    })
  }
}
