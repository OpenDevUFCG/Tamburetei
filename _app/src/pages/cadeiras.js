import { graphql, Link } from 'gatsby'
import PropTypes from 'prop-types'
import React from 'react'

const CadeirasPage = ({ data: { subjects } }) => {
  return (
    <div>
      <ul>
        {subjects.edges.map(subject => (
          <li key={subject.node.id}>
            <Link to={subject.node.fields.slugPath}>
              {subject.node.frontmatter.title}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default CadeirasPage

CadeirasPage.propTypes = {
  data: PropTypes.object.isRequired,
}

export const pageQuery = graphql`
  query AllSubjects {
    subjects: allMarkdownRemark(
      filter: { 
        fileAbsolutePath: { regex: "/README\\.md/" },
        fields: { slug: { regex: "/^\\/[\\w]+\\/$/" } }
      },
      sort: { fields: [frontmatter___title], order: DESC }
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
