import classNames from 'classnames'
import { useStaticQuery, graphql, Link } from 'gatsby'
import PropTypes from 'prop-types'
import React from 'react'

import Layout from '../components/Layout'
import SEO from '../components/SEO'

import styles from './cadeiras.module.css'

const SUBJECTS_QUERY = graphql`
  {
    subjects: allMarkdownRemark(
      filter: {
        fileAbsolutePath: { regex: "/README\\.md/" }
        fields: { slug: { regex: "/^\\/[\\w]+\\/$/" } }
      }
      sort: { fields: [frontmatter___title], order: ASC }
    ) {
      edges {
        node {
          id
          frontmatter {
            title
          }
          fields {
            slugPath
          }
          excerpt
        }
      }
    }
  }
`

const CadeirasPage = () => {
  const data = useStaticQuery(SUBJECTS_QUERY)

  return (
    <Layout className={styles.container}>
      <SEO />
      <h2 className={styles.title}>Disciplinas</h2>
      <section className={styles.section}>
        {data.subjects.edges.map(subject => (
          <div key={subject.node.id} className={styles.cadeiraWrapper}>
            <Link
              to={subject.node.fields.slugPath}
              className={classNames('link', styles.cadeirasLink)}
            >
              {subject.node.frontmatter.title}
            </Link>
            <p>{subject.node.excerpt}</p>
          </div>
        ))}
      </section>
    </Layout>
  )
}

CadeirasPage.propTypes = {
  location: PropTypes.object.isRequired,
}

export default CadeirasPage
