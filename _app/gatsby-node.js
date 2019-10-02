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
    if (!subject.node.fields.path) {
      console.log('esse node', subject)
    }
    createPage({
      path: subject.node.fields.path,
      component: subjectPage,
      context: {
        slug: subject.node.fields.slug,
        path: subject.node.fields.path,
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
      name: 'path',
      node,
      value: value.replace(/([A-Z])/g, (_, v) => '-' + v.toLowerCase()),
    })
  }
}
