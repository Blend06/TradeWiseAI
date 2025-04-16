import React from 'react';

const AppRoute = ({ component: Component, layout: Layout, ...rest }) => {
  Layout = Layout || (props => <React.Fragment>{props.children}</React.Fragment>);

  return (
    <Layout>
      <Component {...rest} />
    </Layout>
  );
};

export default AppRoute;
