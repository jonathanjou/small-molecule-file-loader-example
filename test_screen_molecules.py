from molecule_screener import screen_molecule
import structure

def test_everything_in_one_go():
    st = structure.load('test_target.maegz')
    r_st = structure.load('reference_complex.maegz')
    g = gridgen.load('test_grid.grd')
    tpo = {
        'energy': True,
        'num_poses': 672,
    }
    rt = -1

    s, ds, sc = screen_molecule('test_st.mae', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_st.mae.gz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_st.maegz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_st.sdf', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_st.sdf.gz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_st.sdfgz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_csv.csv', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_csv.csv.gz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
    s, ds, sc = screen_molecule('test_csv.csvgz', st, g, tpo, rt)
    assert s
    assert sc ==  8.13418631   # expected score for this docking example
    assert structure.are_identical(ds, r_st)
