import classNames from 'classnames'
import { useStaticQuery, graphql, Link } from 'gatsby'
import PropTypes from 'prop-types'
import React, { useState } from 'react'

import Layout from './Layout'
import styles from './SubjectLayout.module.scss'
import IconMenu from './IconMenu'

const SubjectLayout = ({ children, location }) => {
  const data = useStaticQuery(graphql`
  {
    subjects: allMarkdownRemark(
      filter: { 
        fileAbsolutePath: { regex: "/README\\.md/" },
        fields: { slug: { regex: "/^\\/[\\w]+\\/$/" } }
      },
      sort: { fields: [frontmatter___title], order: ASC }
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
`)

  const [sideNavOpen, setSideNavOpen] = useState(false)

  return (
    <Layout>
      <div className={styles.container}>
        <div className={styles.sideNavContainer}>
          <div className={styles.sideNavToggle}>
            <button
              className={styles.sideNavToggleButton}
              aria-label={sideNavOpen ? 'Abrir menu' : 'Fechar menu'}
              onClick={() => {
                setSideNavOpen(prevOpen => !prevOpen)
              }}
            >
              <IconMenu close={sideNavOpen} />
            </button>{' '}
            <span className={styles.sideNavToggleText}>Disciplinas</span>
          </div>
          <aside
            className={classNames(styles.sideNav, {
              [styles.sideNavOpen]: sideNavOpen,
            })}
          >
            <nav className={styles.innerNav}>
              {data.subjects.edges.map(subject => (
                <Link
                  className={classNames(styles.linkWrapper, {
                    [styles.linkActive]:
                      location.pathname === subject.node.fields.slugPath,
                  })}
                  key={subject.node.id}
                  to={subject.node.fields.slugPath}
                >
                  {subject.node.frontmatter.title}
                </Link>
              ))}
            </nav>
          </aside>
        </div>
        <section className={styles.content}>{children}</section>
      </div>
    </Layout>
  )
}

SubjectLayout.propTypes = {
  children: PropTypes.node,
  location: PropTypes.object.isRequired,
}

export default SubjectLayout
