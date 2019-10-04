const path = require('path')
const visit = require('unist-util-visit')

module.exports = ({ markdownAST, getNode, markdownNode }) => {
  const parentNode = getNode(markdownNode.parent)
  const basePath = parentNode.root + path.dirname(parentNode.relativePath)

  visit(markdownAST, 'link', link => {
    const isRelativeUrl = !/https?:/.test(link.url)

    if (!isRelativeUrl) {
      return
    }

    if (!link.url.length || link.url.startsWith('#')) {
      return
    }

    const resolvedPath = path
      .resolve(basePath, link.url)
      .replace(/\.md$/, '')
      .replace(/([A-Z])/g, (_, v) => '-' + v.toLowerCase())

    link.url = resolvedPath
  })

  return markdownAST
}
