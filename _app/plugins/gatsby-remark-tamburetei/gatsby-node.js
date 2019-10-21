const { createFilePath } = require('gatsby-source-filesystem')

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
