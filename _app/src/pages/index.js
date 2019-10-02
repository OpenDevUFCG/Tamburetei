import PropTypes from 'prop-types'
import { graphql, Link } from 'gatsby'
import React from 'react'

import Layout from '../components/Layout'
import SEO from '../components/SEO'

const IndexPage = ({ data: { subjects } }) => (
  <Layout>
    <SEO />
    <h1>Oi pessoas!</h1>
    <ul>
      {subjects.edges.map(subject => (
        <li key={subject.node.id}>
          <Link to={subject.node.fields.slugPath}>
            {subject.node.fields.slug}
          </Link>
        </li>
      ))}
    </ul>
  </Layout>
)

IndexPage.propTypes = {
  data: PropTypes.object.isRequired,
}

export default IndexPage

export const pageQuery = graphql`
  query AllSubjects {
    subjects: allMarkdownRemark(
      filter: { fileAbsolutePath: { regex: "/tamburetei/[\\w\\d]+/README.md$/i" } }
    ) {
      edges {
        node {
          id
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
