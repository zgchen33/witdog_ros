#ifndef QUADRUPED_DESCRIPTION_H
#define QUADRUPED_DESCRIPTION_H

#include <quadruped_base/quadruped_base.h>

namespace champ
{
    namespace URDF
    {
        void loadFromHeader(champ::QuadrupedBase &base)
        {
      base.lf.hip.setOrigin(0.08652, 0.028001, -0.005647, 0.0, 0.0, 0.0);
base.lf.upper_leg.setOrigin(-0.0057834, 0.014959, -0.00061935, 0.0, 0.0, 0.0);
base.lf.lower_leg.setOrigin(-0.00091985, 0.0079405, -0.066613, 0.0, 0.0, 0.0);
     base.lf.foot.setOrigin(-0.0098189, 0.0015, -0.059121, 0.0, 0.0, 0.0);

      base.rf.hip.setOrigin(0.08652, -0.028, -0.005647, 0.0, 0.0, 0.0);
base.rf.upper_leg.setOrigin(-0.0057834, -0.014959, -0.00061935, 0.0, 0.0, 0.0);
base.rf.lower_leg.setOrigin(-0.000919872443398681, -0.00834054054053998, -0.0666128977412097, 0.0, 0.0, 0.0);
     base.rf.foot.setOrigin(-0.0091444, -0.0010914, -0.05939, 0.0, 0.0, 0.0);

      base.lh.hip.setOrigin(-0.08248, 0.028001, -0.005937, 0.0, 0.0, 0.0);
base.lh.upper_leg.setOrigin(-0.00578344744545112, 0.0149594594594723, -0.000619354785077068, 0.0, 0.0, 0.0);
base.lh.lower_leg.setOrigin(-0.000919847336912388, 0.00794054054057377, -0.0666130631353466, 0.0, 0.0, 0.0);
     base.lh.foot.setOrigin(-0.0094743, 0.0015, -0.059258, 0.0, 0.0, 0.0);

      base.rh.hip.setOrigin(-0.08248, -0.028, -0.005937, 0.0, 0.0, 0.0);
base.rh.upper_leg.setOrigin(-0.00578344744554893, -0.0149594594594607, -0.000619354785075757, 0.0, 0.0, 0.0);
base.rh.lower_leg.setOrigin(-0.000919872443398723, -0.00834054054054026, -0.0666128977412097, 0.0, 0.0, 0.0);
     base.rh.foot.setOrigin(-0.0092382, -0.0010914, -0.059352, 0.0, 0.0, 0.0);
        }
    }
}
#endif